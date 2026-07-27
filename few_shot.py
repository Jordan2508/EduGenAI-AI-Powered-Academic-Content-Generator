def categorize_length(self, line_count):
    if line_count < 5:
        return "Short"
    elif 5 <= line_count <= 10:
        return "Medium"
    else:
        return "Long"