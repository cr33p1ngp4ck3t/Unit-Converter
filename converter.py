import streamlit as st
import pint
ureg = pint.UnitRegistry()

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.header("Converter App")
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0381ab, #93a9b3);
        background-attachment: fixed;
        color: white;
    }
    .stApp {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)

categories = {
    "Length": ["nautical mile", "mile", "kilometer", "meter", "yard", "foot", "decimeter", "inch", "centimeter", "millimeter"],
    "Weight": ["metric ton", "kilogram", "pound", "ounce", "gram", "milligram"],
    "Volume": ["barrel", "cubic meter", "gallon", "liter", "quart", "pint", "cup", "tablespoon", "teaspoon", "fluid ounce", "milliliter"],
    "Temperature": ["Kelvin", "Celsius", "Fahrenheit"],
    "Time": ["year", "month", "week", "day", "hour", "minute", "second"],
    "Speed": ["knots", "miles per hour", "kilometers per hour", "meters per second"],
    "Area": ["square kilometer", "hectare", "acre", "square mile", "square yard", "square foot", "square inch", "square meter", "square centimeter", "square millimeter"],
    "Energy": ["kilowatt-hour", "watt-hour", "kilocalorie", "calorie", "kilojoule", "joule"],
    "Power": ["gigawatt", "megawatt", "kilowatt", "watt", "horsepower"],
    "Pressure": ["megapascal", "kilopascal", "pascal", "bar", "atmosphere", "torr"],
    "Data": ["petabyte", "terabyte", "gigabyte", "megabyte", "kilobyte", "byte", "bit"],
    "Frequency": ["gigahertz", "megahertz", "kilohertz", "hertz"],
    "Angle": ["degree", "radian", "gradian"],
    "Force": ["kilonewton", "newton", "dyne", "pound-force"]
}

choice = st.selectbox("Select the type of Unit Conversion: ", list(categories.keys()), placeholder="Select", index=None)

if choice:
    st.subheader(f"Conversion for {choice}")

    try:
        fromUnit = st.selectbox("From", categories[choice], index=None, placeholder="Select Any Unit to Convert")
        toUnit = st.selectbox("To", categories[choice], index=None, placeholder="Select Any Unit to Convert")
        value = st.number_input("Enter the value to convert: ", value=1.0)
        quantity = value * getattr(ureg, fromUnit)
        converted_quantity = quantity.to(getattr(ureg, toUnit))
        st.write(f"{value} {fromUnit} is equal to {converted_quantity}.")
    except:
        st.warning("Please Choose a Unit to Convert")
