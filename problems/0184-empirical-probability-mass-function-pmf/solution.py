def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    if samples == []:
        return []

    pmf = []    

    freq_map = {}

    for sample in samples:
        if sample in freq_map:
            freq_map[sample] += 1
        else:
            freq_map[sample] = 1

    for sample in freq_map:
        pmf.append((sample, freq_map[sample] / len(samples)))


    return pmf            

