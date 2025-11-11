from modules.config import Settings
from modules.target import TargetManager

def main():

    print("Starting target authorization check...")
    settings = Settings()
    target_str = "example.com"  # Replace with actual target input
    target_manager = TargetManager(target=target_str, settings=settings)


    authorized_target = target_manager.get_target()
    print(f"Authorized target: {authorized_target}")



if __name__ == "__main__":
    main()