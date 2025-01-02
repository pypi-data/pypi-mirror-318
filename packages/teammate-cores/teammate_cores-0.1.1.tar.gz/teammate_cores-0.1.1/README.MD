```bash
maturin develop  --target x86_64-unknown-linux-gnu
```

```bash
cargo test --color=always --package teammate --lib test::tests::test_main --no-fail-fast --  --exact -Z unstable-options --show-output
```
