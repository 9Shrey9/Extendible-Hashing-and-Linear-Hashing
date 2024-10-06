import React, { useState } from "react";
import axios from "axios";
import { RingLoader } from "react-spinners";
import "./App.css";

function App() {
  const [insertKey, setInsertKey] = useState("");
  const [insertValue, setInsertValue] = useState("");
  const [deleteKey, setDeleteKey] = useState("");
  const [searchKey, setSearchKey] = useState("");
  const [searchResult, setSearchResult] = useState(null);
  const [notification, setNotification] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedHashing, setSelectedHashing] = useState("extendible");
  const [hashTableState, setHashTableState] = useState(null);

  const handleInsert = async (e) => {
    e.preventDefault();
    if (!insertKey || !insertValue) {
      addNotification("error", "Key and Value must be provided for insertion.");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post(
        `http://127.0.0.1:5000/${selectedHashing}/insert`,
        {
          key: parseInt(insertKey),
          value: insertValue,
        },
      );

      if (response.data) {
        addNotification(
          "success",
          `Inserted (${response.data.inserted.key}, ${response.data.inserted.value}) successfully.`,
        );
        setHashTableState(response.data.state);
      } else {
        throw new Error("Invalid response structure");
      }

      setInsertKey("");
      setInsertValue("");
    } catch (error) {
      const errorMessage =
        error.response?.data?.error || "Error inserting data: " + error.message;
      addNotification("error", errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (e) => {
    e.preventDefault();
    if (!deleteKey) {
      addNotification("error", "Key must be provided for deletion.");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.delete(
        `http://127.0.0.1:5000/${selectedHashing}/delete`,
        {
          data: { key: parseInt(deleteKey) },
        },
      );

      if (response.data) {
        addNotification("success", response.data.message);
        setHashTableState(response.data.state);
      } else {
        throw new Error("Invalid response structure");
      }

      setDeleteKey("");
    } catch (error) {
      const errorMessage =
        error.response?.data?.error || "Error deleting data: " + error.message;
      addNotification("error", errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!searchKey) {
      addNotification("error", "Key must be provided for search.");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.get(
        `http://127.0.0.1:5000/${selectedHashing}/search?key=${searchKey}`,
      );

      if (response.data) {
        if (response.data.message) {
          setSearchResult(response.data.message);
          addNotification(
            "success",
            `Found key ${searchKey}: ${response.data.message}`,
          );
        } else {
          addNotification("info", `Key ${searchKey} not found.`);
        }
        setHashTableState(response.data.state);
      } else {
        throw new Error("Invalid response structure");
      }

      setSearchKey("");
    } catch (error) {
      const errorMessage =
        error.response?.data?.error || "Error searching data: " + error.message;
      addNotification("error", errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const addNotification = (type, message) => {
    const newNotification = { id: new Date().getTime(), type, message };
    setNotification((prev) => [...prev, newNotification]);
  };

  const handleReset = () => {
    setInsertKey("");
    setInsertValue("");
    setDeleteKey("");
    setSearchKey("");
    setSearchResult(null);
    setNotification([]);
    setHashTableState(null);
  };

  const renderHashTableState = () => {
    if (!hashTableState) return null;

    // Identify the type of hashing based on unique properties
    const isLinearHashing = hashTableState.current_size !== undefined;
    const isExtendibleHashing = hashTableState.current_level !== undefined;

    return (
      <div className="hash-table-state">
        <h2>Hash Table State</h2>

        {/* Linear Hashing Display */}
        {isLinearHashing && (
          <>
            <h3>Linear Hashing State</h3>
            <p>
              <strong>Current Size:</strong> {hashTableState.current_size}
            </p>
            <p>
              <strong>Entry Count:</strong> {hashTableState.entry_count}
            </p>
            <p>
              <strong>Load Factor:</strong>{" "}
              {hashTableState.load_factor.toFixed(2)}
            </p>

            {/* Display Index Table */}
            <h3>Linear Hashing - Index Table</h3>
            <table className="hash-table">
              <thead>
                <tr>
                  <th>Bucket Index</th>
                  <th>Bucket Content</th>
                </tr>
              </thead>
              <tbody>
                {/* Safely iterate over bucket_contents to render the contents */}
                {hashTableState.bucket_contents &&
                  Object.entries(hashTableState.bucket_contents).map(
                    ([index, content]) => (
                      <tr key={index}>
                        <td>{index}</td>
                        <td>
                          {content.length > 0
                            ? JSON.stringify(content)
                            : "Empty"}
                        </td>
                      </tr>
                    ),
                  )}
              </tbody>
            </table>
          </>
        )}

        {/* Extendible Hashing Display */}
        {isExtendibleHashing && (
          <>
            <h3>Extendible Hashing State</h3>
            <p>
              <strong>Current Level (Global Depth):</strong>{" "}
              {hashTableState.current_level}
            </p>
            <p>
              <strong>Bucket Count:</strong> {hashTableState.bucket_count}
            </p>

            {/* Global Depth Information */}
            <h3>Extendible Hashing - Directory</h3>
            <p>
              <strong>Global Depth:</strong> {hashTableState.current_level}
            </p>

            {/* Local Depths Section */}
            <h3>Local Depths</h3>
            <ul>
              {hashTableState.local_depths &&
                Object.entries(hashTableState.local_depths).map(
                  ([index, depth]) => (
                    <li key={index}>
                      Bucket {index}: Local Depth {depth}
                    </li>
                  ),
                )}
            </ul>

            {/* Directory Content Table */}
            <h3>Index Table</h3>
            <table className="hash-table">
              <thead>
                <tr>
                  <th>Directory</th>
                  <th>Bucket Content</th>
                </tr>
              </thead>
              <tbody>
                {/* Display bucket contents for extendible hashing */}
                {hashTableState.bucket_contents &&
                  Object.entries(hashTableState.bucket_contents).map(
                    ([index, content]) => (
                      <tr key={index}>
                        <td>{index}</td>
                        <td>
                          {content.length > 0
                            ? JSON.stringify(content)
                            : "Empty"}
                        </td>
                      </tr>
                    ),
                  )}
              </tbody>
            </table>
          </>
        )}
      </div>
    );
  };

  return (
    <div className="app-container">
      <div className="App">
        <div className="main-content">
          <h1>Hash Table Visualization</h1>
          <div>
            <label>Select Hashing Method:</label>
            <select
              value={selectedHashing}
              onChange={(e) => setSelectedHashing(e.target.value)}
              style={{ margin: "10px 0" }}
            >
              <option value="extendible">Extendible Hashing</option>
              <option value="linear">Linear Hashing</option>
            </select>
          </div>

          <form onSubmit={handleInsert} className="form-section">
            <h2>Insert</h2>
            <input
              type="number"
              placeholder="Key"
              value={insertKey}
              onChange={(e) => setInsertKey(e.target.value)}
            />
            <input
              type="text"
              placeholder="Value"
              value={insertValue}
              onChange={(e) => setInsertValue(e.target.value)}
            />
            <button type="submit">Insert</button>
          </form>

          <form onSubmit={handleDelete} className="form-section">
            <h2>Delete</h2>
            <input
              type="number"
              placeholder="Key"
              value={deleteKey}
              onChange={(e) => setDeleteKey(e.target.value)}
            />
            <button type="submit">Delete</button>
          </form>

          <form onSubmit={handleSearch} className="form-section">
            <h2>Search</h2>
            <input
              type="number"
              placeholder="Key"
              value={searchKey}
              onChange={(e) => setSearchKey(e.target.value)}
            />
            <button type="submit">Search</button>
          </form>

          {loading && (
            <div className="loading-indicator">
              <RingLoader size={50} color={"#123abc"} loading={loading} />
            </div>
          )}

          <div className="reset-container">
            <button onClick={handleReset}>Reset</button>
          </div>

          {searchResult && (
            <div className="search-result">
              <h3>Search Result:</h3>
              <p>{searchResult}</p>
            </div>
          )}

          {renderHashTableState()}
        </div>

        <div className="notification-panel">
          <h2>Notifications</h2>
          {notification.map((note) => (
            <div key={note.id} className={`notification ${note.type}`}>
              <span>{note.message}</span>
              <button
                onClick={() =>
                  setNotification(notification.filter((n) => n.id !== note.id))
                }
              >
                ✖
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
