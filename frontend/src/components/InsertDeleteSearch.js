// import React, { useState } from 'react';
// import axios from 'axios';
// import { ToastContainer, toast } from 'react-toastify';
// import 'react-toastify/dist/ReactToastify.css';

// const InsertDeleteSearch = () => {
//     const [key, setKey] = useState('');
//     const [value, setValue] = useState('');
//     const [searchKey, setSearchKey] = useState('');
//     const [searchResult, setSearchResult] = useState(null);

//     const handleInsert = async () => {
//         if (!key || !value) {
//             toast.error("Key and value must be provided.");
//             return;
//         }

//         try {
//             const response = await axios.post('/extendible/insert', {
//                 key: parseInt(key, 10), // Convert key to an integer
//                 value: value,
//             });
//             toast.success("Key inserted successfully!");
//             setKey(''); // Reset key input
//             setValue(''); // Reset value input
//         } catch (error) {
//             toast.error(error.response?.data?.error || 'Error inserting key');
//         }
//     };

//     const handleDelete = async () => {
//         if (!key) {
//             toast.error("Key must be provided for deletion.");
//             return;
//         }

//         try {
//             await axios.delete('/extendible/delete', {
//                 data: { key: parseInt(key, 10) }, // Convert key to an integer
//             });
//             toast.success("Key deleted successfully!");
//             setKey(''); // Reset key input
//         } catch (error) {
//             toast.error(error.response?.data?.error || 'Error deleting key');
//         }
//     };

//     const handleSearch = async () => {
//         if (!searchKey) {
//             toast.error("Key must be provided for search.");
//             return;
//         }

//         try {
//             const response = await axios.get('/extendible/search', {
//                 params: { key: parseInt(searchKey, 10) }, // Convert key to an integer
//             });
//             setSearchResult(response.data); // Set search result to state
//             toast.success("Key found!");
//         } catch (error) {
//             toast.error(error.response?.data?.error || 'Error searching for key');
//             setSearchResult(null); // Reset search result on error
//         }
//     };

//     return (
//         <div>
//             <h2>Hash Table Operations</h2>

//             {/* Insert Section */}
//             <div>
//                 <h3>Insert Key</h3>
//                 <input
//                     type="number"
//                     placeholder="Enter key"
//                     value={key}
//                     onChange={(e) => setKey(e.target.value)}
//                 />
//                 <input
//                     type="text"
//                     placeholder="Enter value"
//                     value={value}
//                     onChange={(e) => setValue(e.target.value)}
//                 />
//                 <button onClick={handleInsert}>Insert</button>
//             </div>

//             {/* Delete Section */}
//             <div>
//                 <h3>Delete Key</h3>
//                 <input
//                     type="number"
//                     placeholder="Enter key to delete"
//                     value={key}
//                     onChange={(e) => setKey(e.target.value)}
//                 />
//                 <button onClick={handleDelete}>Delete</button>
//             </div>

//             {/* Search Section */}
//             <div>
//                 <h3>Search Key</h3>
//                 <input
//                     type="number"
//                     placeholder="Enter key to search"
//                     value={searchKey}
//                     onChange={(e) => setSearchKey(e.target.value)}
//                 />
//                 <button onClick={handleSearch}>Search</button>
//                 {searchResult && <div>Result: {JSON.stringify(searchResult)}</div>}
//             </div>

//             <ToastContainer />
//         </div>
//     );
// };

// export default InsertDeleteSearch;
