# Problem Statement

Students and hobbyists learning orbital mechanics often have to work through
the same repetitive calculations by hand — circular orbital velocity, escape
velocity, orbital period, and the two-burn Hohmann transfer between orbits.
Doing this manually is slow and error-prone, and there is no easy way to keep
a record of what has already been calculated during a study session.

## Scope

This project is a command-line **Orbital Mechanics Calculator** that:

- Computes circular orbital velocity, escape velocity, and orbital period
  for any altitude above Earth's surface.
- Plans a Hohmann transfer between two circular orbits, returning the
  required burns (Δv1, Δv2), total Δv, and transfer time.
- Logs every calculation performed in a session to a local JSON file and can
  print a summary report on demand.

Out of scope: non-circular (elliptical) starting orbits, orbits around
bodies other than Earth, and a graphical/web interface (this is a CLI tool).

## Target Users

- Aerospace/physics students who want to check hand-worked orbital mechanics
  problems.
- Space enthusiasts and hobbyists experimenting with mission-planning "what
  ifs" (e.g., "what's the Δv from LEO to GEO?").
- Instructors who want a quick reference tool for classroom demonstrations.

## High-Level Features

1. **Orbital Calculations** — orbital velocity, escape velocity, and
   orbital period for a given altitude.
2. **Hohmann Transfer Planner** — full burn-by-burn breakdown and transfer
   time between two circular orbits.
3. **Mission Log & Reporting** — persistent history of every calculation
   run, with a printable analytics summary (counts by type, most recent
   runs).
