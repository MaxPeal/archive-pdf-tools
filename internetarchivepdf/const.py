VERSION = '1.4.6'

PRODUCER = 'Internet Archive PDF %s; including '\
           'mupdf and pymupdf/skimage' % (VERSION,)


IMAGE_MODE_PASSTHROUGH = 0
IMAGE_MODE_PIXMAP = 1
IMAGE_MODE_MRC = 2
IMAGE_MODE_SKIP = 3


DENOISE_NONE = 'none'
DENOISE_FAST = 'fast'
DENOISE_BREGMAN = 'bregman'

RECODE_RUNTIME_WARNING_INVALID_PAGE_SIZE = 'invalid-page-size'
RECODE_RUNTIME_WARNING_INVALID_PAGE_NUMBERS = 'invalid-page-numbers'
RECODE_RUNTIME_WARNING_INVALID_JP2_HEADERS = 'invalid-jp2-headers'
RECODE_RUNTIME_WARNING_TOO_SMALL_TO_DOWNSAMPLE = 'too-small-to-downsample'

RECODE_RUNTIME_WARNINGS = {
    RECODE_RUNTIME_WARNING_INVALID_PAGE_SIZE,
    RECODE_RUNTIME_WARNING_INVALID_PAGE_NUMBERS,
    RECODE_RUNTIME_WARNING_INVALID_JP2_HEADERS,
    RECODE_RUNTIME_WARNING_TOO_SMALL_TO_DOWNSAMPLE,
}

JPEG2000_IMPL_KAKADU = 'kakadu'
JPEG2000_IMPL_OPENJPEG = 'openjpeg'
JPEG2000_IMPL_GROK = 'grok'
# Pillow is read only
JPEG2000_IMPL_PILLOW = 'pillow'

COMPRESSOR_JPEG2000 = 'jpeg2000'
COMPRESSOR_JPEG = 'jpeg'

__version__ = VERSION
