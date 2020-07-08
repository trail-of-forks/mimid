# Python Library for the Mimid Grammar Extraction Algorithm

This is an implementation of the
[Mimid](https://doi.org/10.5281/zenodo.3876969) algorithm. It has been
modified by Trail of Bits to be a standalone Python library rather than
a set of scripts. The original, upstream version is hosted
[in this Github repository](https://github.com/vrthra/mimid).

The [`mimid`](https://github.com/trailofbits/mimid/tree/mimid) branch of this
repository tracks upstream changes to allow for easier merging to and from
upstream. _All modifications that are intended to be pushed upstream should
be implemented on a fork of the `mimid` branch, not `master`_!

The intent of this library is to be used in conjunction with
[PolyTracker](https://github.com/trailofbits/polytracker) for automated
program instrumentation.

## License

The content and the source code of this project are licensed under
[The Fuzzing Book License](https://github.com/uds-se/fuzzingbook/blob/master/LICENSE.md).
