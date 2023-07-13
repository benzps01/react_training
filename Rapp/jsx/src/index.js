// 1) Import React and ReactDOM libraries
import React from "react";
import ReactDOM from "react-dom/client";

// 2) Get a reference to the div with ID root
// 3) Tell React to take control of that element
const root = ReactDOM.createRoot(document.getElementById("root"));

// 4) Create a component
function App() {
  return (
    <input
      type="text"
      list={[1, 2, 3]}
      style={{ color: "red", border: "3px solid" }}
      autoFocus={true}
    />
  );
}

// 5) Show component on the screen
root.render(<App />);
