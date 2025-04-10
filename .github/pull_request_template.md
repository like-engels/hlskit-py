# HlsKit Pull Request Template

Thank you for contributing to HlsKit! Whether you’re submitting changes here, forking the project, or building extensions, you’re part of our community. We’d love for you to share your work with us—let’s build something great together!

> By submitting this pull request, I agree to the [HlsKit Contributor License Agreement (CLA)](../CLA.md), which ensures our ecosystem thrives under LGPLv3.  
> Everyone modifying HlsKit is a contributor! We encourage you to license your changes under LGPLv3 and make them available to others, fostering collaboration across the community.

## Description

Provide a clear and concise summary of what this PR does. Explain the problem it solves or the feature it adds.

**Example:**  
"This PR adds support for runtime backend selection between FFmpeg and GStreamer, allowing users to choose their preferred video processing engine."

## Related Ticket

Link to the issue this PR addresses, if applicable. Use "Closes #<issue-number>" if it resolves the issue.

**Example:**  
Closes #15

## Changes Made

List the specific changes introduced by this PR. Include new files, modified modules, or other relevant updates.

**Example:**  

- Added `VideoBackend` enum in `src/models/`.  
- Implemented GStreamer processor stub in `src/services/`.  

## Acceptance Criteria

Define the conditions that must be met for this PR to be considered complete. These should align with the feature’s goals or bug fix requirements.

**Example:**  

- Users can toggle between FFmpeg and GStreamer backends at runtime.  
- Output playlists and segments are identical across both backends.  
- Unit tests pass for both code paths.

## Test Plans

Describe how you tested your changes. Include commands, manual steps, or specific scenarios validated.

**Example:**  

- Ran `pytest` to verify unit tests for FFmpeg and GStreamer paths.  
- Manually tested playlist output integrity with sample MP4 files using both backends.  
- Confirmed no regressions in existing FFmpeg functionality.

## Dependencies

If this PR introduces new dependencies, list them and justify their inclusion. If none, state "No new dependencies."

**Example:**  
No new dependencies.

## Checklist

- [ ] I've followed [PEP 8](https://peps.python.org/pep-0008/) style guidelines and ran `ruff format`.
- [ ] My code is clean, well-documented, and tested (unit and/or integration tests added where applicable).
- [ ] I've used the custom exceptions in `tools/hlskit_exceptions.py` for error handling.
- [ ] I've used async/await correctly with `asyncio` where needed.
- [ ] For major changes, I've discussed this in an issue first (link: #<issue-number>).
- [ ] I've reviewed the [project structure](#project-structure) and placed my changes in the appropriate module.

## Additional Notes

Add any extra context, such as performance considerations, trade-offs, or questions for reviewers.

**Example:**  
"The GStreamer stub is minimal for now—future PRs will expand its functionality. Feedback on the backend toggle approach welcome!"

---

Thank you for helping make HlsKit an efficient and powerful video streaming toolkit!
