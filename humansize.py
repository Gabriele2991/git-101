SUFFIXES = ['KB', 'MB', 'GB', 'TB','PB', 'EB', 'ZB', 'YB']


def approximate_size(size):
    """COnvert a file size to a human-readable form"""
    multiple = 1024
    for suffix in SUFFIXES:
        size /= multiple
        if size<multiple:
            return f'{size}{suffix}'
    raise ValueError('number too large')
