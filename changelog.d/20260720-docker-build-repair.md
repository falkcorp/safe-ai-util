### Fixed

#### The container image builds, and the binary in it runs

Four faults, each hidden behind the previous: `.dockerignore` excluded the
`Cargo.lock` the Dockerfile copies; `adduser` no longer exists in the Debian 13
base; `benches/` was required by a `[[bench]]` declaration but never copied; and
the runtime stage ran an older Debian than the builder, so the image built
cleanly while the binary died with "GLIBC_2.39 not found".
