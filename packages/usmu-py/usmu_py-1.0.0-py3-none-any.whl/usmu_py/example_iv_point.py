from usmu_py.smu import USMU
import numpy as np

def main():
    port = "COM39"   # Change to your actual port
    voltages = np.linspace(0, 1, 2, 3)  # 0, 0.5, 1.0, ..., 5.0

    with USMU(port=port, baudrate=9600) as smu:
        print("IDN:", smu.read_idn())

        # Configure SMU
        smu.enable_output()
        smu.set_current_limit(100.0)   # 100 mA
        smu.set_oversample_rate(25)    # example

        results = []
        for v in voltages:
            voltage, current = smu.measure_iv_point(v)
            results.append((voltage, current))
            print(f"Set {v:.2f} V, Measured: {voltage:.3f} V, {current*1e3:.3f} mA")

        smu.disable_output()

    # Save data or do further analysis
    with open("iv_data.csv", "w") as f:
        f.write("Voltage_V,Current_A\n")
        for (v, i) in results:
            f.write(f"{v},{i}\n")

if __name__ == "__main__":
    main()
