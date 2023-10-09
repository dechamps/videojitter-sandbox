import videojitter.testing


async def videojitter_test(test_case):
    pipeline = videojitter.testing.Pipeline(test_case)
    await pipeline.run_generate_spec()
    await pipeline.run_generate_fake_recording(
        "--clock-skew",
        1,
        "--pattern-count",
        0,
        "--white-duration-overshoot",
        0,
        "--even-duration-overshoot",
        0,
        "--dc-offset",
        0,
        "--gaussian-filter-stddev-seconds",
        0,
        "--high-pass-filter-hz",
        0,
        "--noise-rms-per-hz",
        0,
    )
    await pipeline.run_analyze_recording()
    await pipeline.run_generate_report()