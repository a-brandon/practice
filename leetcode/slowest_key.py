def slowestKey(releaseTimes, keysPressed):
    times = {keysPressed[0]: releaseTimes[0]}

    for i, _ in enumerate(releaseTimes[1:], 1):
        duration = releaseTimes[i] - releaseTimes[i - 1]
        if keysPressed[i] not in times:
            times[keysPressed[i]] = duration
        elif keysPressed[i] in times:
            if duration > times[keysPressed[i]]:
                times[keysPressed[i]] = duration

    return max(k for k, v in times.items() if v == max(times.values()))