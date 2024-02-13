import datetime

def get_time_period():
    current_time = datetime.datetime.now().time()
    if current_time.hour < 12:
        return 'Good morning'
    elif current_time.hour < 18:
        return 'Good afternoon'
    else:
        return 'Good evening'

def main():
    message = get_time_period()
    print(message)

if __name__ == "__main__":
    main()
