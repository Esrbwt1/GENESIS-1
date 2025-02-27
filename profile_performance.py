# profile_performance.py
import cProfile
import pstats

def main():
    # Import the main function from main.py
    from main import main as genesis_main
    genesis_main()

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    # Create a Stats object and print the top 20 functions sorted by cumulative time.
    stats = pstats.Stats(profiler).sort_stats('cumulative')
    stats.print_stats(20)