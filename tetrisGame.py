import multiprocessing
from implementationAI import ImplementationAI
from implementation import Implementation


def run_human_mode():
    impl = Implementation()
    impl.play()

def run_ai_mode():
    impl_ai = ImplementationAI()
    impl_ai.play()
    
if __name__ == '__main__':
    # Create two separate processes for human mode and AI mode
    p1 = multiprocessing.Process(target=run_human_mode)
    p2 = multiprocessing.Process(target=run_ai_mode)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()      