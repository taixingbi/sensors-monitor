import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import sensors from './app/sensors';
import update from './app/update';
import test from './app/test';

function App() {
  return (

    <div >
      <div>
        <Router>
            <Switch>
              <Route path="/update/:id/" component={update} />
              <Route path="/test/" component={test} />

              <Route path="/" component={sensors} />

            </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;