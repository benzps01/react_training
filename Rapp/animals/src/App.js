function App() {
  const handleClick = () => {
    console.log("Buton was clicked!");
  };

  return (
    <div>
      <button onClick={handleClick}>Add Animal</button>
    </div>
  );
}

export default App;
