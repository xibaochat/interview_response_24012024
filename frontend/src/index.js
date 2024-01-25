import React from "react";
import ReactDOM from "react-dom/client";
import { useEffect } from 'react';
import {
    BrowserRouter as Router,
    Routes,
    Route, useNavigate
} from 'react-router-dom';

import defaultCat from "./components/defaultCat.jpg";
import Calculator from "./components/Calculator";

const NoPage = ({imageUrl}) => {
    return <div style={{ backgroundImage: imageUrl }}>
        <h1>404</h1>
        </div>;
};


function App() {
    const imageUrl = "url(https://akie.b-cdn.net/landingPage.png)";
	const navigate = useNavigate();
    useEffect(() => {
        document.title = 'Akie42';
    }, []);
    useEffect(() => {
        document.title = 'Akie42';
    }, []);

  let routes = (
	<Routes>
          <Route path="/" element={<img src={defaultCat} alt="petit chat" navigate={navigate}/>}/>
          <Route path="/calculator" element={<Calculator/>}/>
          <Route path="/*" element={<NoPage imageUrl={imageUrl}/>} />
    </Routes>
  );


    return (
            <div>
            {routes}
            </div>
    );
}

const rootElement = document.getElementById("root")
const root = ReactDOM.createRoot(rootElement);
root.render(
    <Router>
      <App />
    </Router>
);
