import os
import platform
import subprocess
import time
from typing import Optional

class ChessAgent:
    def __init__(self):
        self.process: Optional[subprocess.Popen] = None
        self.engine_path = self._get_engine_path()
        self.is_initialized = False
        self._validate_system()  # التحقق من أن النظام يدعم المحرك
        self.initialize_engine()

    def _validate_system(self):
        """يتحقق من أن النظام المستخدم هو Linux."""
        if platform.system() != "Linux":
            raise EnvironmentError("This chess engine works only on Linux systems.")

    def _get_engine_path(self) -> str:
        """يحدد مسار المحرك الثنائي."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        engine_path = os.path.join(current_dir, "binaries", "bbc_1_engin")
        if not os.path.exists(engine_path):
            raise FileNotFoundError("Chess engine file not found!")
        return engine_path

    def initialize_engine(self) -> None:
        """يبدأ تشغيل المحرك ويجهزه للاستخدام."""
        try:
            self.process = subprocess.Popen(
                self.engine_path,
                universal_newlines=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                bufsize=1,
            )
            self._configure_engine()
            self.is_initialized = True
        except Exception as e:
            print(f"Engine initialization error: {e}")
            self.close()

    def _configure_engine(self):
        """يضبط إعدادات المحرك."""
        commands = [
            "uci",
            "setoption name Threads value 1",
            "setoption name Hash value 4",
            "isready",
        ]
        for cmd in commands:
            self._send_command(cmd)
            if cmd == "uci":
                self._wait_for("uciok")
            elif cmd == "isready":
                self._wait_for("readyok")

    def _send_command(self, command: str) -> None:
        """يرسل الأوامر إلى المحرك."""
        if self.process and self.process.stdin:
            try:
                self.process.stdin.write(f"{command}\n")
                self.process.stdin.flush()
            except IOError as e:
                print(f"Error sending command: {e}")
                self.initialize_engine()

    def _wait_for(self, target: str, timeout: float = 1.0) -> bool:
        """ينتظر استجابة معينة من المحرك."""
        start_time = time.time()
        while self.process and time.time() - start_time < timeout:
            if self.process.stdout:
                line = self.process.stdout.readline().strip()
                if target in line:
                    return True
            time.sleep(0.001)
        return False

    def get_best_move(self, fen: str, remaining_time: int) -> str:
        """يحصل على أفضل حركة باستخدام FEN."""
        if not self.is_initialized:
            self.initialize_engine()
        think_time = min(max(remaining_time // 30, 100), 500)  # وقت التفكير

        try:
            self._send_command(f"position fen {fen}")
            self._send_command(f"go movetime {think_time}")
            start_time = time.time()
            best_move = None
            while time.time() - start_time < (think_time / 1000 + 0.1):
                if self.process and self.process.stdout:
                    line = self.process.stdout.readline().strip()
                    if line.startswith("bestmove"):
                        best_move = line.split()[1]
                        break
            if not best_move:
                self.initialize_engine()
                return self.get_best_move(fen, remaining_time)
            return best_move
        except Exception as e:
            print(f"Error during move calculation: {e}")
            self.initialize_engine()
            return "e2e4"

    def close(self) -> None:
        """يغلق المحرك."""
        try:
            if self.process:
                self._send_command("quit")
                self.process.stdin.close()
                self.process.terminate()
                self.process.wait(timeout=1.0)
        except Exception as e:
            print(f"Error during cleanup: {e}")
        finally:
            self.process = None
            self.is_initialized = False
