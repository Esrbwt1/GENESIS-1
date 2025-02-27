# profile_performance.py
import cProfile
import pstats
import os

def main():
    # Import the main function from main.py
    from main import main as genesis_main
    
    # Run in CI mode if detected
    if os.environ.get('CI') == 'true':
        print("\n[PROFILER] Running in CI mode - disabling interactive features")
        genesis_main(ci_mode=True)
    else:
        genesis_main()

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    
    # Create a Stats object and print the top 20 functions
    stats = pstats.Stats(profiler).sort_stats('cumulative')
    print("\n=== PROFILING RESULTS ===")
    stats.print_stats(20)
    
    # Save results to file
    stats.dump_stats('profile_results.prof')
    print("\n[PROFILER] Saved profile results to profile_results.prof")