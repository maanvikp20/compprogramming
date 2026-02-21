# 4 kyu - human readable duration format

def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    result = []
    time_units = [
        ("year", 365*24*60*60),
        ("day", 24*60*60),
        ("hour", 60*60),
        ("minute", 60),
        ("second", 1)
    ]

    for name, unit_seconds in time_units:
        if seconds >= unit_seconds:
            count = seconds // unit_seconds
            seconds = seconds % unit_seconds
            # pluralize immediately
            if count == 1:
                result.append(f"{count} {name}")
            else:
                result.append(f"{count} {name}s")
            
    if len(result) == 1:
        return result[0]
    
    return ", ".join(result[:-1]) + " and " + result[-1]


print(format_duration(242062374))