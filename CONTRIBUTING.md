# Contribution Guide for HlsKit-Py

Love HlsKit? Join our community! Whether you’re submitting changes directly, forking the project, or building extensions, you’re a contributor to the HlsKit ecosystem. We’d love for you to share your work with us—let’s build something great together!

> HlsKit is licensed under LGPLv3. By modifying or distributing it (e.g., via forks, wrappers, libraries or extensions), you agree to the [HlsKit Contributor License Agreement (CLA)](CLA.md), which ensures our ecosystem thrives.
> Everyone who modifies HlsKit is part of our community! We encourage you to license your changes under LGPLv3 and make them available to others, fostering collaboration across
> To prevent abuse, we encourage developers using modified versions in networked applications to make their source code available, in the spirit of the AGPL

## Introduction

HlsKit-Py is a Python library that provides tools for converting video files into adaptive bitrate HLS streams using `ffmpeg`. It mirrors the capabilities of the Rust version (HlsKit) and is designed with scalability, performance, and clarity in mind. Community contributions are welcome and encouraged to improve functionality, add features, and maintain code quality.

## General Guidelines

1. **Be respectful and constructive** in all communications.
2. **Follow best practices** in Python development, and always prioritize code readability and correctness.
3. **Raise issues** for bugs, features, or improvements before submitting major changes.

## Dependencies

HlsKit-Py relies on the following core dependencies:

- `pydantic`
- `ruff`

Before introducing any new dependency, please open a discussion or issue to justify its addition.

## Project Structure

The project is structured for clarity and maintainability:

```
src/hlskit_py
├── models
│   ├── hls_video_processing_settings.py
│   └── hls_video.py
├── services
│   └── hls_video_processor.py
└── tools
    ├── ffmpeg_command_builder.py
    └── m3u8_tools.py
```

- **models/**: Data models and configuration schemas.
- **services/**: Business logic and orchestration of video processing.
- **tools/**: Utility modules like FFmpeg command builders and M3U8 helpers.

## Testing

Unit tests are highly encouraged. Include them alongside any core feature or logic change. Prefer `pytest` and use fixtures for reusable test data.

## Error Handling

Use idiomatic Python exception handling. Wrap subprocess calls and file operations with informative error messages. Avoid suppressing exceptions silently.

## Code Style

We use `ruff` for linting and formatting. Please run it before submitting a PR:

```bash
ruff check .
```

Stick to [PEP8](https://pep8.org/) and modern Python practices (e.g., type hints, Pydantic models).

## Async Execution

HlsKit-Py is designed to be fully asynchronous using `asyncio` and `subprocess`. Any long-running or IO-bound operation must be async to ensure scalability.

## Submitting New Features

When submitting a new feature, please include the following information in your issue or PR:

**Example Feature Request:**

**Description:**
Add support for parallel video processing batches.

**Changes Required:**

- Update `HlsVideoProcessor` to accept batch inputs.
- Add new settings to configure concurrency.

**Acceptance Criteria:**

- Users can submit multiple videos for processing.
- Output is consistent and validated.

**Test Plans:**

- Async test suite to cover batch submissions.

## Submitting a Pull Request (PR)

Use this format for PRs:

**Description:**
Implements `--output-format` option to choose between TS and fMP4 segments.

**Related Issue:**
Closes #12

**Changes Made:**

- Modified `ffmpeg_command_builder.py`
- Updated `HlsVideoProcessingSettings`

**Acceptance Criteria:**

- Optionally generate fMP4 segments.
- Backward compatible with default TS behavior.

**Test Plans:**

- Unit test for FFmpeg args with new format.
- Integration test validating output structure.

## Reporting Issues

Open a GitHub issue with this format:

- **Summary** of the issue
- **Steps to Reproduce**
- **Expected Behavior**
- **Actual Behavior**
- **Logs, Stacktrace or Screenshots** if available

---
Thank you for contributing to HlsKit-Py! Your feedback, code, and ideas help build a better open-source video processing toolkit for everyone.
