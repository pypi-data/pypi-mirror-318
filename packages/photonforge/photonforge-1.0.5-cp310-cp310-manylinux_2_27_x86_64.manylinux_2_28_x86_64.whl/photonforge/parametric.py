# No pollution of the parametric namespace
import photonforge as _pf
import numpy as _np

import itertools as _it
import warnings as _warn
import typing as _typ


@_pf.parametric_component
def straight(
    *,
    port_spec: _typ.Union[str, _pf.PortSpec],
    length: float,
    active_model: _typ.Literal["Tidy3D", "Waveguide"] = "Waveguide",
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
    waveguide_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """Straight waveguide section.

    Args:
        port_spec: Port specification describing waveguide cross-section.
        length: Section length.
        active_model: Name of the model to be used by default; must be
          either ``"Tidy3D"`` or ``"Waveguide"``.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.
        waveguide_model_kwargs: Dictionary of keyword arguments passed to
          the component's :class:`photonforge.WaveguideModel`.

    Returns:
        Component with the straight section, ports and model.
    """
    if technology is None:
        technology = _pf.config.default_technology
    if isinstance(port_spec, str):
        port_spec = technology.ports[port_spec]

    c = _pf.Component(name, technology=technology)
    for layer, path in port_spec.get_paths((0, 0)):
        c.add(layer, path.segment((length, 0)))
    c.add_port(_pf.Port((0, 0), 0, port_spec))
    c.add_port(_pf.Port((length, 0), 180, port_spec, inverted=True))

    c.add_model(_pf.WaveguideModel(**dict(waveguide_model_kwargs)), "Waveguide", False)

    model_kwargs = {"port_symmetries": [("P0", "P1", {"P1": "P0"})]}
    model_kwargs.update(tidy3d_model_kwargs)
    c.add_model(_pf.Tidy3DModel(**model_kwargs), "Tidy3D", False)

    c.activate_model(active_model)
    return c


@_pf.parametric_component
def transition(
    *,
    port_spec1: _typ.Union[str, _pf.PortSpec],
    port_spec2: _typ.Union[str, _pf.PortSpec],
    length: float,
    constant_length: float = 0,
    profile: _typ.Union[str, _pf.Expression] = None,
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """Straight waveguide that works as a transition between port profiles.

    Args:
        port_spec1: Port specification describing the first cross-section.
        port_spec2: Port specification describing the second cross-section.
        length: Transition length.
        constant_length: Constant cross-section length added to both ends.
        profile: String expression describing the transition shape
          parametrized by the independent variable ``"u"``, ranging from 0
          to 1 along the transition. The expression must evaluate to a float
          between 0 and 1 representing the weight of the second profile with
          respect to the first at that position. Alternatively, an
          :class:`photonforge.Expression` with 1 parameter can be used. If
          ``None``, a linear transition is used.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.

    Returns:
        Component with the transition geometry, ports and model.
    """
    if length <= 0 and constant_length <= 0:
        raise ValueError("Transition length cannot be 0.")

    if profile is None:

        def interp(a, b):
            return b
    else:
        if isinstance(profile, _pf.Expression):
            parameter = profile.parameters
            if len(parameter) != 1:
                raise TypeError("Profile expression must contain 1 parameter only.")
            expressions = profile.expressions
            if len(expressions) == 0:
                raise TypeError("Profile expression must contain at least 1 expression.")
        elif isinstance(profile, str):
            parameter = ["u"]
            expressions = [("p", profile)]

        value_name = expressions[-1][0]

        def interp(a, b):
            return _pf.Expression(
                parameter,
                expressions
                + [
                    f"{a} + {value_name} * {b - a}",
                    f"{b - a}",
                ],
            )

    if technology is None:
        technology = _pf.config.default_technology
    if isinstance(port_spec1, str):
        port_spec1 = technology.ports[port_spec1]
    if isinstance(port_spec2, str):
        port_spec2 = technology.ports[port_spec2]
    only1 = set(layer for _, _, layer in port_spec1.path_profiles)
    only2 = set(layer for _, _, layer in port_spec2.path_profiles)
    both = only1.intersection(only2)
    only1 -= both
    only2 -= both
    c = _pf.Component(name, technology=technology)
    start_point = (constant_length, 0)
    mid_point = (constant_length + length, 0)
    end_point = (2 * constant_length + length, 0)
    for layer in only1:
        for w1, g1, l1 in port_spec1.path_profiles:
            if l1 != layer:
                continue
            path = _pf.Path((0, 0), w1, g1)
            if constant_length > 0:
                path.segment(start_point, (w1, "constant"), (g1, "constant"))
            if length > 0:
                path.segment(mid_point, width=interp(w1, 0))
            c.add(layer, path)
    for layer in only2:
        for w2, g2, l2 in port_spec2.path_profiles:
            if l2 != layer:
                continue
            path = _pf.Path(start_point, 0, g2)
            if length > 0:
                path.segment(mid_point, width=interp(0, w2))
            if constant_length > 0:
                path.segment(end_point, (w2, "constant"), (g2, "constant"))
            c.add(layer, path)
    for layer in both:
        prof1 = sorted((g, w) for w, g, l1 in port_spec1.path_profiles if l1 == layer)
        prof2 = sorted((g, w) for w, g, l2 in port_spec2.path_profiles if l2 == layer)
        combinations = zip(prof1, prof2) if len(prof1) == len(prof2) else _it.product(prof1, prof2)
        for (g1, w1), (g2, w2) in combinations:
            path = _pf.Path((0, 0), w1, g1)
            if constant_length > 0:
                path.segment(start_point, (w1, "constant"), (g1, "constant"))
            if length > 0:
                path.segment(mid_point, width=interp(w1, w2), offset=interp(g1, g2))
            else:
                c.add(layer, path)
                path = _pf.Path(mid_point, w2, g2)
            if constant_length > 0:
                path.segment(end_point, (w2, "constant"), (g2, "constant"))
            c.add(layer, path)
    c.add_port(_pf.Port((0, 0), 0, port_spec1))
    c.add_port(_pf.Port(end_point, 180, port_spec2, inverted=True))
    c.add_model(_pf.Tidy3DModel(**dict(tidy3d_model_kwargs)), "Tidy3D")
    return c


@_pf.parametric_component
def bend(
    *,
    port_spec: _typ.Union[str, _pf.PortSpec],
    radius: _typ.Optional[float] = None,
    angle: float = 90,
    euler_fraction: float = 0,
    active_model: _typ.Literal["Tidy3D", "Waveguide"] = "Waveguide",
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
    waveguide_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """Waveguide bend section.

    Args:
        port_spec: Port specification describing waveguide cross-section.
        radius: Central arc radius.
        angle: Arc coverage angle.
        euler_fraction: Fraction of the bend that is created using an Euler
          spiral (see :func:`photonforge.Path.arc`).
        active_model: Name of the model to be used by default; must be
          either ``"Tidy3D"`` or ``"Waveguide"``.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.
        waveguide_model_kwargs: Dictionary of keyword arguments passed to
          the component's :class:`photonforge.WaveguideModel`.

    Returns:
        Component with the circular bend section, ports and model.
    """
    if technology is None:
        technology = _pf.config.default_technology
    if isinstance(port_spec, str):
        port_spec = technology.ports[port_spec]
    if radius is None:
        radius = _pf.config.default_radius

    if angle % 90 != 0:
        _warn.warn(
            "Using bends with angles not multiples of 90° might lead to disconnected waveguides. "
            "Consider building a continuous path with grid-aligned ports instead of connecting "
            "sections with non grid-aligned ports.",
            RuntimeWarning,
            2,
        )

    c = _pf.Component(name, technology=technology)
    c.add_port(_pf.Port((0, 0), 0, port_spec))
    path_length = None
    if angle > 0:
        radians = (angle - 90) / 180.0 * _np.pi
        endpoint = (radius * _np.cos(radians), radius * (1 + _np.sin(radians)))
        for layer, path in port_spec.get_paths((0, 0)):
            path.arc(-90, angle - 90, radius, euler_fraction=euler_fraction, endpoint=endpoint)
            c.add(layer, path)
            if path_length is None:
                path_length = path.length()
        c.add_port(_pf.Port(endpoint, angle - 180, port_spec, inverted=True))
    else:
        radians = (90 + angle) / 180.0 * _np.pi
        endpoint = (radius * _np.cos(radians), radius * (-1 + _np.sin(radians)))
        for layer, path in port_spec.get_paths((0, 0)):
            path.arc(90, 90 + angle, radius, euler_fraction=euler_fraction, endpoint=endpoint)
            c.add(layer, path)
            if path_length is None:
                path_length = path.length()
        c.add_port(_pf.Port(endpoint, angle + 180, port_spec, inverted=True))

    model_kwargs = {"length": path_length}
    model_kwargs.update(waveguide_model_kwargs)
    c.add_model(_pf.WaveguideModel(**model_kwargs), "Waveguide", False)

    model_kwargs = {"port_symmetries": [("P0", "P1", {"P1": "P0"})]}
    model_kwargs.update(tidy3d_model_kwargs)
    c.add_model(_pf.Tidy3DModel(**model_kwargs), "Tidy3D", False)

    c.activate_model(active_model)
    return c


@_pf.parametric_component
def s_bend(
    *,
    port_spec: _typ.Union[str, _pf.PortSpec],
    length: float,
    offset: float,
    euler_fraction: float = 0,
    active_model: _typ.Literal["Tidy3D", "Waveguide"] = "Waveguide",
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
    waveguide_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """S bend waveguide section.

    Args:
        port_spec: Port specification describing waveguide cross-section.
        length: Length of the S bend in the main propagation direction.
        offset: Side offset of the S bend.
        euler_fraction: Fraction of the bends that is created using an Euler
          spiral (see :func:`photonforge.Path.arc`).
        active_model: Name of the model to be used by default; must be
          either ``"Tidy3D"`` or ``"Waveguide"``.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.
        waveguide_model_kwargs: Dictionary of keyword arguments passed to
          the component's :class:`photonforge.WaveguideModel`.

    Returns:
        Component with the S bend section, ports and model.
    """
    if technology is None:
        technology = _pf.config.default_technology
    if isinstance(port_spec, str):
        port_spec = technology.ports[port_spec]

    c = _pf.Component(name, technology=technology)
    path_length = None
    for layer, path in port_spec.get_paths((0, 0)):
        c.add(layer, path.s_bend((length, offset), euler_fraction))
        if path_length is None:
            path_length = path.length()

    c.add_port(_pf.Port((0, 0), 0, port_spec))
    c.add_port(_pf.Port((length, offset), 180, port_spec, inverted=True))

    model_kwargs = {"length": path_length}
    model_kwargs.update(waveguide_model_kwargs)
    c.add_model(_pf.WaveguideModel(**model_kwargs), "Waveguide", False)

    model_kwargs = {"port_symmetries": [("P0", "P1", {"P1": "P0"})]}
    model_kwargs.update(tidy3d_model_kwargs)
    c.add_model(_pf.Tidy3DModel(**model_kwargs), "Tidy3D", False)

    c.activate_model(active_model)
    return c


@_pf.parametric_component
def crossing(
    *,
    port_spec: _typ.Union[str, _pf.PortSpec],
    arm_length: float,
    added_width: _typ.Union[float, str, _pf.Expression] = 0,
    extra_length: float = 0,
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """Straight waveguide section.

    Args:
        port_spec: Port specification describing waveguide cross-section.
        arm_length: Length of a single crossing arm.
        added_width: Width added to the arm linearly up to the center. An
          expression or string (with independent variable ``"u"``) can also
          be used.
        extra_length: Additional length for a straight section at the ports.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.

    Returns:
        Component with the crossing, ports and model.
    """
    if technology is None:
        technology = _pf.config.default_technology
    if isinstance(port_spec, str):
        port_spec = technology.ports[port_spec]

    if isinstance(added_width, _pf.Expression):
        parameter = added_width.parameters
        if len(parameter) != 1:
            raise TypeError("Profile expression must contain 1 parameter only.")
        expressions = added_width.expressions
        if len(expressions) == 0:
            raise TypeError("Profile expression must contain at least 1 expression.")
    elif isinstance(added_width, str):
        parameter = ["u"]
        expressions = [("p", added_width)]
    else:
        parameter = ["u"]
        expressions = [("p", f"{added_width}*u")]

    value_name = expressions[-1][0]

    length = arm_length + extra_length
    bounds = _pf.Rectangle((-length, -length), (length, length))

    c = _pf.Component(name, technology=technology)
    for width, offset, layer in port_spec.path_profiles:
        width_expr = _pf.Expression(
            parameter, expressions + [f"{width} + {value_name}", ("derivative", 0)]
        )
        p0 = _pf.Path((-length, 0), width, offset)
        p1 = _pf.Path((length, 0), width, -offset)
        if extra_length > 0:
            p0.segment((-arm_length, 0))
            p1.segment((arm_length, 0))
        p0.segment((0, 0), width=width_expr)
        p1.segment((0, 0), width=width_expr)
        in_bounds = _pf.boolean(
            [p0, p1, p0.to_polygon().rotate(90), p1.to_polygon().rotate(90)], bounds, "*"
        )
        c.add(layer, *in_bounds)

    c.add_port(_pf.Port((-length, 0), 0, port_spec))
    c.add_port(_pf.Port((0, -length), 90, port_spec))
    c.add_port(_pf.Port((length, 0), 180, port_spec, inverted=True))
    c.add_port(_pf.Port((0, length), -90, port_spec, inverted=True))

    c.add_model(_pf.Tidy3DModel(**dict(tidy3d_model_kwargs)), "Tidy3D")
    return c


@_pf.parametric_component
def ring_coupler(
    *,
    port_spec: _typ.Union[str, _pf.PortSpec, tuple],
    coupling_distance: float,
    radius: _typ.Optional[float] = None,
    bus_length: float,
    euler_fraction: float = 0.0,
    coupling_length: float = 0.0,
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """Ring/straight coupling region.

    Args:
        port_spec: Port specification describing waveguide cross-section.
          A tuple with 2 values can be used, one for each coupler side.
        coupling_distance: Distance between bus and ring waveguide centers.
        radius: Central ring radius.
        bus_length: Length of the bus waveguide added each side of the
          straight coupling section. If both ``bus_length`` and
          ``coupling_length`` are 0, the bus waveguide is not included.
        euler_fraction: Fraction of the bends that is created using an Euler
          spiral (see :func:`photonforge.Path.arc`).
        coupling_length: Length of straigh coupling region.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.

    Returns:
        Coupling component.
    """
    if technology is None:
        technology = _pf.config.default_technology
    if radius is None:
        radius = _pf.config.default_radius

    if isinstance(port_spec, str):
        port_spec = (technology.ports[port_spec], technology.ports[port_spec])
    elif isinstance(port_spec, _pf.PortSpec):
        port_spec = (port_spec, port_spec)
    else:
        port_spec = list(port_spec)
        for i in range(2):
            if isinstance(port_spec[i], str):
                port_spec[i] = technology.ports[port_spec[i]]

    c = _pf.Component(name, technology=technology)

    xp = bus_length + 0.5 * coupling_length
    yp = -radius - coupling_distance
    xr = radius + 0.5 * coupling_length
    if xp > 0:
        for layer, path in port_spec[0].get_paths((-xp, yp)):
            c.add(layer, path.segment((xp, yp)))
    for layer, path in port_spec[1].get_paths((xr, 0)):
        path.arc(0, -90, radius, euler_fraction=euler_fraction)
        if coupling_length > 0:
            path.segment((-0.5 * coupling_length, -radius))
        path.arc(-90, -180, radius, endpoint=(-xr, 0), euler_fraction=euler_fraction)
        c.add(layer, path)

    if xp > 0:
        c.add_port(_pf.Port((-xp, yp), 0, port_spec[0]))
    c.add_port(_pf.Port((-xr, 0), -90, port_spec[1], inverted=True))
    if xp > 0:
        c.add_port(_pf.Port((xp, yp), 180, port_spec[0], inverted=True))
    c.add_port(_pf.Port((xr, 0), -90, port_spec[1]))

    model_kwargs = {}
    if xp == 0:
        model_kwargs["port_symmetries"] = [("P0", "P1", {"P1": "P0"})]
    model_kwargs.update(tidy3d_model_kwargs)
    c.add_model(_pf.Tidy3DModel(**model_kwargs), "Tidy3D")
    return c


@_pf.parametric_component
def s_bend_ring_coupler(
    *,
    port_spec: _typ.Union[str, _pf.PortSpec, tuple],
    coupling_distance: float,
    radius: _typ.Optional[float] = None,
    s_bend_length: float,
    s_bend_offset: float,
    euler_fraction: float = 0.0,
    coupling_length: float = 0.0,
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """Ring coupling through an S bend curve.

    Args:
        port_spec: Port specification describing waveguide cross-section.
          A tuple with 2 values can be used, one for each coupler side.
        coupling_distance: Distance between bus and ring waveguide centers.
        radius: Central ring radius.
        s_bend_length: Length of the S bends.
        s_bend_offset: Offset of the S bends.
        euler_fraction: Fraction of the bends that is created using an Euler
          spiral (see :func:`photonforge.Path.arc`).
        coupling_length: Length of straigh coupling region.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.

    Returns:
        Coupling component.
    """
    if technology is None:
        technology = _pf.config.default_technology
    if isinstance(port_spec, str):
        port_spec = (technology.ports[port_spec], technology.ports[port_spec])
    elif isinstance(port_spec, _pf.PortSpec):
        port_spec = (port_spec, port_spec)
    else:
        port_spec = list(port_spec)
        for i in range(2):
            if isinstance(port_spec[i], str):
                port_spec[i] = technology.ports[port_spec[i]]
    if radius is None:
        radius = _pf.config.default_radius

    c = _pf.Component(name, technology=technology)

    xs = s_bend_length + 0.5 * coupling_length
    ys = -radius - coupling_distance - s_bend_offset
    y_mid = -radius - coupling_distance
    for layer, path in port_spec[0].get_paths((-xs, ys)):
        path.s_bend((-0.5 * coupling_length, y_mid), euler_fraction)
        if coupling_length > 0:
            path.segment((0.5 * coupling_length, y_mid))
        path.s_bend((xs, ys), euler_fraction)
        c.add(layer, path)

    xr = radius + 0.5 * coupling_length
    for layer, path in port_spec[1].get_paths((xr, 0)):
        path.arc(0, -90, radius, euler_fraction=euler_fraction)
        if coupling_length > 0:
            path.segment((-0.5 * coupling_length, -radius))
        path.arc(-90, -180, radius, endpoint=(-xr, 0), euler_fraction=euler_fraction)
        c.add(layer, path)

    c.add_port(_pf.Port((-xs, ys), 0, port_spec[0]))
    c.add_port(_pf.Port((-xr, 0), -90, port_spec[1], inverted=True))
    c.add_port(_pf.Port((xs, ys), 180, port_spec[0], inverted=True))
    c.add_port(_pf.Port((xr, 0), -90, port_spec[1]))

    c.add_model(_pf.Tidy3DModel(**dict(tidy3d_model_kwargs)), "Tidy3D")
    return c


@_pf.parametric_component
def dual_ring_coupler(
    *,
    port_spec: _typ.Union[str, _pf.PortSpec, tuple],
    coupling_distance: float,
    radius: _typ.Optional[float] = None,
    euler_fraction: float = 0.0,
    coupling_length: float = 0.0,
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """Dual ring coupling region.

    Args:
        port_spec: Port specification describing waveguide cross-section.
          A tuple with 2 values can be used, one for each coupler side.
        coupling_distance: Distance between bus and ring waveguide centers.
        radius: Central ring radius.
        euler_fraction: Fraction of the bends that is created using an Euler
          spiral (see :func:`photonforge.Path.arc`).
        coupling_length: Length of straigh coupling region.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.

    Returns:
        Coupling component.
    """
    if technology is None:
        technology = _pf.config.default_technology
    if isinstance(port_spec, str):
        port_spec = (technology.ports[port_spec], technology.ports[port_spec])
    elif isinstance(port_spec, _pf.PortSpec):
        port_spec = (port_spec, port_spec)
    else:
        port_spec = list(port_spec)
        for i in range(2):
            if isinstance(port_spec[i], str):
                port_spec[i] = technology.ports[port_spec[i]]
    if radius is None:
        radius = _pf.config.default_radius

    c = _pf.Component(name, technology=technology)

    xr = radius + 0.5 * coupling_length
    yr = 2 * radius + coupling_distance
    for layer, path in port_spec[0].get_paths((-xr, -yr)):
        path.arc(180, 90, radius, euler_fraction=euler_fraction)
        if coupling_length > 0:
            path.segment((0.5 * coupling_length, -radius - coupling_distance))
        path.arc(90, 0, radius, endpoint=(xr, -yr), euler_fraction=euler_fraction)
        c.add(layer, path)

    for layer, path in port_spec[1].get_paths((xr, 0)):
        path.arc(0, -90, radius, euler_fraction=euler_fraction)
        if coupling_length > 0:
            path.segment((-0.5 * coupling_length, -radius))
        path.arc(-90, -180, radius, endpoint=(-xr, 0), euler_fraction=euler_fraction)
        c.add(layer, path)

    c.add_port(_pf.Port((-xr, -yr), 90, port_spec[0]))
    c.add_port(_pf.Port((-xr, 0), -90, port_spec[1], inverted=True))
    c.add_port(_pf.Port((xr, -yr), 90, port_spec[0], inverted=True))
    c.add_port(_pf.Port((xr, 0), -90, port_spec[1]))

    c.add_model(_pf.Tidy3DModel(**dict(tidy3d_model_kwargs)), "Tidy3D")
    return c


@_pf.parametric_component
def s_bend_coupler(
    *,
    port_spec: _typ.Union[str, _pf.PortSpec, tuple],
    coupling_distance: float,
    s_bend_length: float,
    s_bend_offset: float,
    euler_fraction: float = 0.0,
    coupling_length: float = 0.0,
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """S bend coupling region.

    Args:
        port_spec: Port specification describing waveguide cross-section.
          A tuple with 2 values can be used, one for each coupler side.
        coupling_distance: Distance between waveguide centers.
        s_bend_length: Length of the S bends.
        s_bend_offset: Offset of the S bends.
        euler_fraction: Fraction of the bends that is created using an Euler
          spiral (see :func:`photonforge.Path.arc`).
        coupling_length: Length of straigh coupling region.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.

    Returns:
        Coupling component.
    """
    if technology is None:
        technology = _pf.config.default_technology
    if isinstance(port_spec, str):
        port_spec = (technology.ports[port_spec], technology.ports[port_spec])
    elif isinstance(port_spec, _pf.PortSpec):
        port_spec = (port_spec, port_spec)
    else:
        port_spec = list(port_spec)
        for i in range(2):
            if isinstance(port_spec[i], str):
                port_spec[i] = technology.ports[port_spec[i]]

    c = _pf.Component(name, technology=technology)
    x_out = 2 * s_bend_length + coupling_length
    y_out = 2 * s_bend_offset + coupling_distance
    x_mid = s_bend_length + coupling_length
    y_mid = s_bend_offset + coupling_distance

    for layer, path in port_spec[0].get_paths((0, 0)):
        path.s_bend((s_bend_length, s_bend_offset), euler_fraction)
        if coupling_length > 0:
            path.segment((x_mid, s_bend_offset))
        path.s_bend((x_out, 0), euler_fraction)
        c.add(layer, path)

    for layer, path in port_spec[1].get_paths((x_out, y_out)):
        path.s_bend((x_mid, y_mid), euler_fraction, direction=(-1, 0))
        if coupling_length > 0:
            path.segment((s_bend_length, y_mid))
        path.s_bend((0, y_out), euler_fraction)
        c.add(layer, path)

    c.add_port(_pf.Port((0, 0), 0, port_spec[0]))
    c.add_port(_pf.Port((0, y_out), 0, port_spec[1], inverted=True))
    c.add_port(_pf.Port((x_out, 0), -180, port_spec[0], inverted=True))
    c.add_port(_pf.Port((x_out, y_out), 180, port_spec[1]))

    c.add_model(_pf.Tidy3DModel(**dict(tidy3d_model_kwargs)), "Tidy3D")
    return c


@_pf.parametric_component
def s_bend_straight_coupler(
    *,
    port_spec: _typ.Union[str, _pf.PortSpec, tuple],
    coupling_distance: float,
    s_bend_length: float,
    s_bend_offset: float,
    euler_fraction: float = 0.0,
    coupling_length: float = 0.0,
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """S bend coupling region.

    Args:
        port_spec: Port specification describing waveguide cross-section.
          A tuple with 2 values can be used, one for each coupler side.
        coupling_distance: Distance between waveguide centers.
        s_bend_length: Length of the S bends.
        s_bend_offset: Offset of the S bends.
        euler_fraction: Fraction of the bends that is created using an Euler
          spiral (see :func:`photonforge.Path.arc`).
        coupling_length: Length of straigh coupling region.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.

    Returns:
        Coupling component.
    """
    if technology is None:
        technology = _pf.config.default_technology
    if isinstance(port_spec, str):
        port_spec = (technology.ports[port_spec], technology.ports[port_spec])
    elif isinstance(port_spec, _pf.PortSpec):
        port_spec = (port_spec, port_spec)
    else:
        port_spec = list(port_spec)
        for i in range(2):
            if isinstance(port_spec[i], str):
                port_spec[i] = technology.ports[port_spec[i]]

    c = _pf.Component(name, technology=technology)

    xs = 2 * s_bend_length + coupling_length
    for layer, path in port_spec[0].get_paths((0, 0)):
        c.add(layer, path.segment((xs, 0)))

    x_mid = s_bend_length + coupling_length
    ys = s_bend_offset + coupling_distance
    for layer, path in port_spec[1].get_paths((xs, ys)):
        path.s_bend((x_mid, coupling_distance), euler_fraction, direction=(-1, 0))
        if coupling_length > 0:
            path.segment((s_bend_length, coupling_distance))
        path.s_bend((0, ys), euler_fraction)
        c.add(layer, path)

    c.add_port(_pf.Port((0, 0), 0, port_spec[0]))
    c.add_port(_pf.Port((0, ys), 0, port_spec[1], inverted=True))
    c.add_port(_pf.Port((xs, 0), -180, port_spec[0], inverted=True))
    c.add_port(_pf.Port((xs, ys), 180, port_spec[1]))

    c.add_model(_pf.Tidy3DModel(**dict(tidy3d_model_kwargs)), "Tidy3D")
    return c


@_pf.parametric_component
def rectangular_spiral(
    *,
    port_spec: _typ.Union[str, _pf.PortSpec],
    turns: int,
    radius: _typ.Optional[float] = None,
    separation: float = 0,
    size: tuple[float, float] = (0, 0),
    align_ports: _typ.Literal["", "x", "y"] = "",
    active_model: _typ.Literal["Circuit", "Tidy3D"] = "Circuit",
    technology: _pf.Technology = None,
    name: str = "",
    bend_kwargs: dict[str, _typ.Any] = {},
    straight_kwargs: dict[str, _typ.Any] = {},
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
    circuit_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """Rectangular spiral.

    Args:
        port_spec: Port specification describing waveguide cross-section.
        turns: Number of turns in each of the 2 spiral arms.
        radius: Bend radius for the spiral turns.
        separation: Distance between waveguide centers in parallel sections.
        size: Spiral dimensions measured from the waveguide centers.
        align_ports: Optionally align ports to have centers with same
          ``"x"`` or ``"y"`` coordinates.
        active_model: Name of the model to be used by default; must be
          either ``"Tidy3D"`` or ``"Circuit"``.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        bend_kwargs: Dictionary of keyword arguments for :func:`bend`.
        straight_kwargs: Dictionary of keyword arguments for
          :func:`straight`.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.
        circuit_model_kwargs: Dictionary of keyword arguments passed to
          the component's :class:`photonforge.CircuitModel`.

    Returns:
        Component with the straight section, ports and model.

    Note:
        The full length of the spiral can be computed by summing all path
        lengths from the main component's references, assuming the paths
        in the specified layer have no offsets:
        ``sum(r.component.structures[layer][0].length() for r in spiral.references))``
    """
    if turns < 2:
        raise ValueError("Argument 'turns' must be at least 2.")

    if technology is None:
        technology = _pf.config.default_technology
    if isinstance(port_spec, str):
        port_spec = technology.ports[port_spec]
    if separation <= 0:
        separation = port_spec.width
    if radius is None:
        radius = _pf.config.default_radius

    if align_ports == "x":
        inner_size = [size[0] - 2 * separation, size[1] - separation]
    elif align_ports == "y":
        inner_size = [size[0] - 2 * separation - radius, size[1]]
    else:
        inner_size = [size[0] - 2 * separation, size[1]]

    if turns % 2 == 0:
        inner_size = [inner_size[1], inner_size[0]]

    inner_size[0] -= 4 * radius + ((turns - 2) // 2) * 2 * separation
    inner_size[1] -= 2 * radius + ((turns - 1) // 2) * 2 * separation

    for i in range(2):
        if inner_size[i] < 0:
            j = (1 - i) if turns % 2 == 0 else i
            if size[j] > 0:
                raise ValueError(
                    f"Dimension {size[j]} is too small for the spiral in the {'xy'[j]} axis."
                )
            inner_size[i] = 0

    straight_kwds = dict(straight_kwargs)
    straight_kwds["technology"] = technology
    straight_kwds["port_spec"] = port_spec

    bend_kwds = dict(bend_kwargs)
    bend_kwds["technology"] = technology
    bend_kwds["port_spec"] = port_spec

    straight = _pf.parametric.straight(length=inner_size[1], **straight_kwds)
    bend0 = _pf.parametric.bend(radius=radius, angle=-90, **bend_kwds)
    bend1 = _pf.parametric.bend(radius=radius, angle=90, **bend_kwds)

    c = _pf.Component(name, technology=technology)

    start = c.add_reference(straight)
    if turns % 4 == 1:
        start.rotate(90)
    elif turns % 4 == 2:
        start.rotate(180)
    elif turns % 4 == 3:
        start.rotate(-90)
    arm0 = start
    arm1 = start

    lengths = [inner_size[0] / 2, inner_size[1] + separation]
    for steps in range(turns):
        arm0 = c.add_reference(bend0).connect("P0", arm0["P1"])
        arm1 = c.add_reference(bend1).connect("P1", arm1["P0"])
        i = steps % 2
        if steps < turns - 1 and lengths[i] > 0:
            straight = _pf.parametric.straight(length=lengths[i], **straight_kwds)
            arm0 = c.add_reference(straight).connect("P0", arm0["P1"])
            arm1 = c.add_reference(straight).connect("P1", arm1["P0"])
        if steps == 0:
            lengths[0] += inner_size[0] / 2 + separation + 2 * radius
        else:
            lengths[i] += 2 * separation

    straight = _pf.parametric.straight(
        length=lengths[(turns + 1) % 2] - 2 * separation + radius, **straight_kwds
    )
    arm1 = c.add_reference(straight).connect("P1", arm1["P0"])

    if align_ports == "x":
        straight = _pf.parametric.straight(
            length=lengths[(turns + 1) % 2] - 2 * separation, **straight_kwds
        )
        arm0 = c.add_reference(straight).connect("P0", arm0["P1"])
        arm0 = c.add_reference(bend0).connect("P0", arm0["P1"])
        straight = _pf.parametric.straight(length=lengths[turns % 2], **straight_kwds)
        arm0 = c.add_reference(straight).connect("P0", arm0["P1"])
        arm0 = c.add_reference(bend0).connect("P0", arm0["P1"])
        straight = _pf.parametric.straight(
            length=lengths[(turns + 1) % 2] - separation + radius, **straight_kwds
        )
        arm0 = c.add_reference(straight).connect("P0", arm0["P1"])
    elif align_ports == "y":
        straight = _pf.parametric.straight(
            length=lengths[(turns + 1) % 2] - 2 * separation, **straight_kwds
        )
        arm0 = c.add_reference(straight).connect("P0", arm0["P1"])
        arm0 = c.add_reference(bend0).connect("P0", arm0["P1"])
        straight = _pf.parametric.straight(length=lengths[turns % 2] - separation, **straight_kwds)
        arm0 = c.add_reference(straight).connect("P0", arm0["P1"])
        arm0 = c.add_reference(bend1).connect("P0", arm0["P1"])
    else:
        arm0 = c.add_reference(straight).connect("P0", arm0["P1"])

    if inner_size[1] == 0:
        c.remove(start)

    dx = -arm1["P0"].center
    for ref in c.references:
        ref.translate(dx)

    c.add_port(arm1["P0"])
    c.add_port(arm0["P1"])

    c.add_model(_pf.CircuitModel(**dict(circuit_model_kwargs)), "Circuit", False)

    model_kwargs = {"port_symmetries": [("P0", "P1", {"P1": "P0"})]}
    model_kwargs.update(tidy3d_model_kwargs)
    c.add_model(_pf.Tidy3DModel(**model_kwargs), "Tidy3D", False)

    c.activate_model(active_model)
    return c


def _get_port(
    arg: _typ.Union[_pf.Port, tuple[_pf.Reference, str], tuple[_pf.Reference, str, int]],
) -> _pf.Port:
    if isinstance(arg, _pf.Port):
        return arg
    len_arg = len(arg)
    if (
        len_arg < 2
        or len_arg > 3
        or not isinstance(arg[0], _pf.Reference)
        or not isinstance(arg[1], str)
        or (len_arg == 3 and not isinstance(arg[2], int))
    ):
        raise TypeError(
            "Argument 'port*' must be a Port instance or a tuple with a Reference, the port name, "
            "and, optionally, the reference index in case of a reference array."
        )
    return arg[0].get_ports(arg[1])[0 if len_arg == 2 else arg[2]]


@_pf.parametric_component
def route(
    *,
    port1: _typ.Union[_pf.Port, tuple[_pf.Reference, str], tuple[_pf.Reference, str, int]],
    port2: _typ.Union[_pf.Port, tuple[_pf.Reference, str], tuple[_pf.Reference, str, int]],
    radius: _typ.Optional[float] = None,
    waypoints: _typ.Sequence = (),
    technology: _pf.Technology = None,
    name: str = "",
    straight_kwargs: dict[str, _typ.Any] = {},
    bend_kwargs: dict[str, _typ.Any] = {},
    s_bend_kwargs: dict[str, _typ.Any] = {},
    circuit_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """Route the connection between 2 compatible ports.

    The route is built heuristically from :func:`straight`, :func:`bend`,
    and :func:`s_bend` sections, favoring Manhattan geometry.

    Args:
        port1: First port to be connected. The port can be specfied as a
          :class:`photonforge.Port` or as a tuple including a
          :class:`photonforge.Reference`, the port name, and the repetition
          index (optinal, only for array references).
        port2: Second port to be connected.
        radius: Radius used for bends and S bends.
        waypoints: 2D coordinates used to guide the route.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        straight_kwargs: Dictionary of keyword arguments passed to the
          :func:`straight` function.
        bend_kwargs: Dictionary of keyword arguments passed to the
          :func:`bend` function.
        s_bend_kwargs: Dictionary of keyword arguments passed to the
          :func:`s_bend` function.
        circuit_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.CircuitModel`.

    Returns:
        Component with the route, including ports and model.

    Note:
        Each waypoint can also include the route direction at that point by
        including the angle (in degrees). Angles must be a multiple of 90°.
    """
    port1 = _get_port(port1)
    port2 = _get_port(port2)

    if not (
        (port1.spec.symmetric() and port1.spec == port2.spec)
        or (
            not port1.spec.symmetric()
            and (
                (port1.spec == port2.spec and port1.inverted != port2.inverted)
                or (port1.spec == port2.spec.inverted() and port1.inverted == port2.inverted)
            )
        )
    ):
        raise RuntimeError("Ports have incompatible specifications and cannot be connected.")

    if technology is None:
        technology = _pf.config.default_technology
    if radius is None:
        radius = _pf.config.default_radius

    port_spec = port1.spec if port1.inverted else port1.spec.inverted()

    straight_kwargs = dict(straight_kwargs)
    straight_kwargs["technology"] = technology
    straight_kwargs["port_spec"] = port_spec

    bend_kwargs = dict(bend_kwargs)
    bend_kwargs["technology"] = technology
    bend_kwargs["port_spec"] = port_spec
    bend_kwargs["radius"] = radius

    s_bend_kwargs = dict(s_bend_kwargs)
    s_bend_kwargs["technology"] = technology
    s_bend_kwargs["port_spec"] = port_spec

    wp = _np.empty((len(waypoints), 3))
    for i, p in enumerate(waypoints):
        wp[i, 0] = p[0]
        wp[i, 1] = p[1]
        wp[i, 2] = p[2] % 360 if len(p) > 2 else -1

    component = _pf.Component(name, technology=technology)
    dir0 = (port1.input_direction + 180) % 360
    p0 = _pf.Port(port1.center, dir0, port1.spec, inverted=not port1.inverted)
    dir1 = (port2.input_direction + 180) % 360
    p1 = _pf.Port(port2.center, dir1, port2.spec, inverted=not port2.inverted)
    component.add_port([p0, p1])
    component.add_model(_pf.CircuitModel(**dict(circuit_model_kwargs)), "Circuit")

    return _pf.extension._route(
        component,
        port1,
        port2,
        radius,
        wp,
        straight,
        straight_kwargs,
        bend,
        bend_kwargs,
        s_bend,
        s_bend_kwargs,
    )


@_pf.parametric_component
def route_s_bend(
    *,
    port1: _typ.Union[_pf.Port, tuple[_pf.Reference, str], tuple[_pf.Reference, str, int]],
    port2: _typ.Union[_pf.Port, tuple[_pf.Reference, str], tuple[_pf.Reference, str, int]],
    euler_fraction: float = 0,
    active_model: _typ.Literal["Tidy3D", "Waveguide"] = "Waveguide",
    technology: _pf.Technology = None,
    name: str = "",
    tidy3d_model_kwargs: dict[str, _typ.Any] = {},
    waveguide_model_kwargs: dict[str, _typ.Any] = {},
) -> _pf.Component:
    """Create an S bend connecting 2 compatible ports.

    Args:
        port1: First port to be connected. The port can be specfied as a
          :class:`photonforge.Port` or as a tuple including a
          :class:`photonforge.Reference`, the port name, and the repetition
          index (optinal, only for array references).
        port2: Second port to be connected.
        euler_fraction: Fraction of the bends that is created using an Euler
          spiral (see :func:`photonforge.Path.arc`).
        active_model: Name of the model to be used by default; must be
          either ``"Tidy3D"`` or ``"Waveguide"``.
        technology: Component technology. If ``None``, the default
          technology is used.
        name: Component name.
        tidy3d_model_kwargs: Dictionary of keyword arguments passed to the
          component's :class:`photonforge.Tidy3DModel`.
        waveguide_model_kwargs: Dictionary of keyword arguments passed to
          the component's :class:`photonforge.WaveguideModel`.

    Returns:
        Component with the route, including ports and model.
    """
    port1 = _get_port(port1)
    port2 = _get_port(port2)

    if not (
        (port1.spec.symmetric() and port1.spec == port2.spec)
        or (
            not port1.spec.symmetric()
            and (
                (port1.spec == port2.spec and port1.inverted != port2.inverted)
                or (port1.spec == port2.spec.inverted() and port1.inverted == port2.inverted)
            )
        )
    ):
        raise RuntimeError("Ports have incompatible specifications and cannot be connected.")

    if abs((port1.input_direction - port2.input_direction) % 360 - 180) >= 1e-12:
        raise RuntimeError("Ports must have opposite directions.")

    if technology is None:
        technology = _pf.config.default_technology

    port_spec = port1.spec if port1.inverted else port1.spec.inverted()

    angle = (port1.input_direction - 180) / 180 * _np.pi
    direction = _np.array((_np.cos(angle), _np.sin(angle)))

    c = _pf.Component(name, technology=technology)
    path_length = None
    for layer, path in port_spec.get_paths(port1.center):
        c.add(layer, path.s_bend(port2.center, euler_fraction, direction))
        if path_length is None:
            path_length = path.length()

    c.add_port(_pf.Port(port1.center, port1.input_direction - 180, port_spec))
    c.add_port(_pf.Port(port2.center, port2.input_direction - 180, port_spec, inverted=True))

    model_kwargs = {"length": path_length}
    model_kwargs.update(waveguide_model_kwargs)
    c.add_model(_pf.WaveguideModel(**model_kwargs), "Waveguide", False)

    model_kwargs = {"port_symmetries": [("P0", "P1", {"P1": "P0"})]}
    model_kwargs.update(tidy3d_model_kwargs)
    c.add_model(_pf.Tidy3DModel(**model_kwargs), "Tidy3D", False)

    c.activate_model(active_model)
    return c
