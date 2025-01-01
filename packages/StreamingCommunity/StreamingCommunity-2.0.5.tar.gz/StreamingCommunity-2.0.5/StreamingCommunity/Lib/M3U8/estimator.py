import os
import time
import logging
import threading
from collections import deque


# External libraries
import psutil
from tqdm import tqdm


# Internal utilities
from StreamingCommunity.Util.color import Colors
from StreamingCommunity.Util.os import internet_manager
from StreamingCommunity.Util._jsonConfig import config_manager


# Variable
TQDM_USE_LARGE_BAR = config_manager.get_int('M3U8_DOWNLOAD', 'tqdm_use_large_bar')


class M3U8_Ts_Estimator:
    def __init__(self, total_segments: int):
        """
        Initialize the M3U8_Ts_Estimator object.

        Parameters:
            - total_segments (int): Length of total segments to download.
        """
        self.ts_file_sizes = []
        self.now_downloaded_size = 0
        self.total_segments = total_segments
        self.lock = threading.Lock()
        self.speed = {"upload": "N/A", "download": "N/A"}

        # Only start the speed capture thread if TQDM_USE_LARGE_BAR is True
        if not TQDM_USE_LARGE_BAR:
            self.speed_thread = threading.Thread(target=self.capture_speed)
            self.speed_thread.daemon = True
            self.speed_thread.start()

    def add_ts_file(self, size: int, size_download: int, duration: float):
        """
        Add a file size to the list of file sizes.

        Parameters:
            - size (int): The size of the ts file to be added.
            - size_download (int): Single size of the ts file.
            - duration (float): Time to download segment file.
        """
        if size <= 0 or size_download <= 0 or duration <= 0:
            logging.error("Invalid input values: size=%d, size_download=%d, duration=%f", size, size_download, duration)
            return

        # Add total size bytes
        self.ts_file_sizes.append(size)
        self.now_downloaded_size += size_download

    def capture_speed(self, interval: float = 1, pid: int = None):
        """
        Capture the internet speed periodically for a specific process (identified by PID) 
        or the entire system if no PID is provided.
        """
        
        def get_network_io(process=None):
            """
            Get network I/O counters for a specific process or system-wide if no process is specified.
            """
            try:
                if process:
                    io_counters = process.io_counters()
                    return io_counters
                else:
                    io_counters = psutil.net_io_counters()
                    return io_counters
            except Exception as e:
                logging.warning(f"Unable to access network I/O counters: {e}")
                return None

        # If a PID is provided, attempt to attach to the corresponding process
        process = None
        if pid is not None:
            try:
                process = psutil.Process(pid)
            except psutil.NoSuchProcess:
                logging.error(f"Process with PID {pid} does not exist.")
                return
            except Exception as e:
                logging.error(f"Failed to attach to process with PID {pid}: {e}")
                return

        while True:
            old_value = get_network_io(process)

            if old_value is None:  # If psutil fails, continue with the next interval
                time.sleep(interval)
                continue

            time.sleep(interval)
            new_value = get_network_io(process)

            if new_value is None:  # Handle again if psutil fails in the next call
                time.sleep(interval)
                continue

            with self.lock:

                # Calculate speed based on process-specific counters if process is specified
                if process:
                    upload_speed = (new_value.write_bytes - old_value.write_bytes) / interval
                    download_speed = (new_value.read_bytes - old_value.read_bytes) / interval
                    
                else:
                    # System-wide counters
                    upload_speed = (new_value.bytes_sent - old_value.bytes_sent) / interval
                    download_speed = (new_value.bytes_recv - old_value.bytes_recv) / interval

                self.speed = {
                    "upload": internet_manager.format_transfer_speed(upload_speed),
                    "download": internet_manager.format_transfer_speed(download_speed)
                }


    def get_average_speed(self) -> float:
        """
        Calculate the average internet speed.

        Returns:
            float: The average internet speed in Mbps.
        """
        with self.lock:
            return self.speed['download'].split(" ")

    def calculate_total_size(self) -> str:
        """
        Calculate the total size of the files.

        Returns:
            str: The mean size of the files in a human-readable format.
        """
        try:
            if len(self.ts_file_sizes) == 0:
                raise ValueError("No file sizes available to calculate total size.")

            total_size = sum(self.ts_file_sizes)
            mean_size = total_size / len(self.ts_file_sizes)

            # Return formatted mean size
            return internet_manager.format_file_size(mean_size)

        except ZeroDivisionError as e:
            logging.error("Division by zero error occurred: %s", e)
            return "0B"

        except Exception as e:
            logging.error("An unexpected error occurred: %s", e)
            return "Error"

    def get_downloaded_size(self) -> str:
        """
        Get the total downloaded size formatted as a human-readable string.

        Returns:
            str: The total downloaded size as a human-readable string.
        """
        return internet_manager.format_file_size(self.now_downloaded_size)

    def update_progress_bar(self, total_downloaded: int, duration: float, progress_counter: tqdm) -> None:
        """
        Updates the progress bar with information about the TS segment download.

        Parameters:
            total_downloaded (int): The length of the content of the downloaded TS segment.
            duration (float): The duration of the segment download in seconds.
            progress_counter (tqdm): The tqdm object representing the progress bar.
        """
        # Add the size of the downloaded segment to the estimator
        self.add_ts_file(total_downloaded * self.total_segments, total_downloaded, duration)

        # Get downloaded size and total estimated size
        downloaded_file_size_str = self.get_downloaded_size()
        file_total_size = self.calculate_total_size()

        # Fix parameter for prefix
        number_file_downloaded = downloaded_file_size_str.split(' ')[0]
        number_file_total_size = file_total_size.split(' ')[0]
        units_file_downloaded = downloaded_file_size_str.split(' ')[1]
        units_file_total_size = file_total_size.split(' ')[1]

        # Update the progress bar's postfix
        if TQDM_USE_LARGE_BAR:
            average_internet_speed = self.get_average_speed()[0]
            average_internet_unit = self.get_average_speed()[1]
            progress_counter.set_postfix_str(
                f"{Colors.WHITE}[ {Colors.GREEN}{number_file_downloaded} {Colors.WHITE}< {Colors.GREEN}{number_file_total_size} {Colors.RED}{units_file_total_size} "
                f"{Colors.WHITE}| {Colors.CYAN}{average_internet_speed} {Colors.RED}{average_internet_unit}"
            )

        else:
            progress_counter.set_postfix_str(
                f"{Colors.WHITE}[ {Colors.GREEN}{number_file_downloaded}{Colors.RED} {units_file_downloaded} "
                f"{Colors.WHITE}| {Colors.CYAN}N/A{Colors.RED} N/A"
            )