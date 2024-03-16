import React, { useState, useEffect } from 'react'
// useState contains data retrieved from the backend and used to render data
// useEffect fetch backend api on first render

function App() {
  //data is a set variable, setdata is a function that manipulates data

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("http://localhost:5000/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  return (
    <div>
    {(typeof data.members === 'undefined') ? (
      <div>
        Loading...
      </div>
    ) : (
      data.members.map((member, i) => (
        <p key={i}>{member}</p>
      ))
    )}
     
      </div>
  )
}

export default App