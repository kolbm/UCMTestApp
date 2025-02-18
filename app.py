import streamlit as st
import math

def main():
    st.image("https://raw.githubusercontent.com/kolbm/UCMTestApp/main/Image%20Edits.png", use_container_width=True)
    st.title("Uniform Circular Motion Formula Selector")
    st.write("Select the type of problem and enter the given values. The app will suggest the correct formula.")

    problem_type = st.selectbox("Select Problem Type:", [
        "Period & Frequency",
        "Angular & Tangential Velocity",
        "Centripetal Acceleration",
        "Centripetal Force"
    ])

    if problem_type == "Period & Frequency":
        st.subheader("Period & Frequency Calculator")
        st.latex(r"T = \frac{t}{n}, \quad f = \frac{1}{T}")
        given = st.radio("What is given?", ["Time for multiple cycles", "Frequency", "Period"])
        
        if given == "Time for multiple cycles":
            n = st.number_input("Number of cycles (n):", min_value=1, value=10)
            t = st.number_input("Total time (s):", min_value=0.01, value=5.0)
            if st.button("Calculate"):
                T = t / n
                f = 1 / T
                st.success(f"Period (T) = {T:.3f} s, Frequency (f) = {f:.3f} Hz")
        elif given == "Frequency":
            f = st.number_input("Frequency (Hz):", min_value=0.01, value=5.0)
            if st.button("Calculate"):
                T = 1 / f
                st.success(f"Period (T) = {T:.3f} s")
        elif given == "Period":
            T = st.number_input("Period (s):", min_value=0.01, value=5.0)
            if st.button("Calculate"):
                f = 1 / T
                st.success(f"Frequency (f) = {f:.3f} Hz")

    elif problem_type == "Angular & Tangential Velocity":
        st.subheader("Angular & Tangential Velocity Calculator")
        st.latex(r"\omega = \frac{2\pi}{T}, \quad v = \omega r")
        r = st.number_input("Radius (m):", min_value=0.01, value=2.0)
        given = st.radio("What is given?", ["Period", "Frequency", "Angular Velocity"])
        
        if given == "Period":
            T = st.number_input("Period (s):", min_value=0.01, value=5.0)
            if st.button("Calculate"):
                omega = 2 * math.pi / T
                v = omega * r
                st.success(f"Angular Velocity (ω) = {omega:.3f} rad/s, Tangential Velocity (v) = {v:.3f} m/s")
        elif given == "Frequency":
            f = st.number_input("Frequency (Hz):", min_value=0.01, value=1.0)
            if st.button("Calculate"):
                omega = 2 * math.pi * f
                v = omega * r
                st.success(f"Angular Velocity (ω) = {omega:.3f} rad/s, Tangential Velocity (v) = {v:.3f} m/s")
        elif given == "Angular Velocity":
            omega = st.number_input("Angular Velocity (rad/s):", min_value=0.01, value=2.0)
            if st.button("Calculate"):
                v = omega * r
                st.success(f"Tangential Velocity (v) = {v:.3f} m/s")

    elif problem_type == "Centripetal Acceleration":
        st.subheader("Centripetal Acceleration Calculator")
        st.latex(r"a_c = \frac{v^2}{r}")
        given = st.radio("What is given?", ["Velocity & Radius", "Acceleration & Radius"])
        
        if given == "Velocity & Radius":
            v = st.number_input("Velocity (m/s):", min_value=0.01, value=5.0)
            r = st.number_input("Radius (m):", min_value=0.01, value=2.0)
            if st.button("Calculate"):
                a_c = v**2 / r
                st.success(f"Centripetal Acceleration (a_c) = {a_c:.3f} m/s²")
        elif given == "Acceleration & Radius":
            a_c = st.number_input("Centripetal Acceleration (m/s²):", min_value=0.01, value=2.0)
            r = st.number_input("Radius (m):", min_value=0.01, value=2.0)
            if st.button("Calculate"):
                v = math.sqrt(a_c * r)
                st.success(f"Velocity (v) = {v:.3f} m/s")

    elif problem_type == "Centripetal Force":
        st.subheader("Centripetal Force Calculator")
        st.latex(r"F_c = \frac{m v^2}{r}")
        given = st.radio("What is given?", ["Mass, Velocity & Radius", "Force & Mass"])
        
        if given == "Mass, Velocity & Radius":
            m = st.number_input("Mass (kg):", min_value=0.01, value=1.0)
            v = st.number_input("Velocity (m/s):", min_value=0.01, value=5.0)
            r = st.number_input("Radius (m):", min_value=0.01, value=2.0)
            if st.button("Calculate"):
                F_c = (m * v**2) / r
                st.success(f"Centripetal Force (F_c) = {F_c:.3f} N")
        elif given == "Force & Mass":
            F_c = st.number_input("Centripetal Force (N):", min_value=0.01, value=10.0)
            m = st.number_input("Mass (kg):", min_value=0.01, value=1.0)
            if st.button("Calculate"):
                a_c = F_c / m
                st.success(f"Centripetal Acceleration (a_c) = {a_c:.3f} m/s²")

if __name__ == "__main__":
    main()
