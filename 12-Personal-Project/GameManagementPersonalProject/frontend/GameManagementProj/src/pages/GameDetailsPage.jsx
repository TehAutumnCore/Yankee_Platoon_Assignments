import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { apiService } from '../services/api';

const GameDetailsPage = () => {
   const { id } = useParams();
   const { token, isAuthenticated } = useAuth();
   const [game, setGame] = useState(null);
   const [loading, setLoading] = useState(true);
   const [error, setError] = useState('');
   const [addingToLibrary, setAddingToLibrary] = useState(false);
   const [libraryMessage, setLibraryMessage] = useState('');
   const [isInLibrary, setIsInLibrary] = useState(false);

   useEffect(() => {
       const fetchGameDetails = async () => {
           try {
               const response = await apiService.getGameById(id);
               const data = await response.json();
               console.log('Game details:', data);
               setGame(data);
           } catch (err) {
               console.error('Error fetching game details:', err);
               setError('Failed to load game details');
           } finally {
               setLoading(false);
           }
       };

       fetchGameDetails();
   }, [id]);

   useEffect(() => {
       const checkLibraryStatus = async () => {
           if (isAuthenticated && token) {
               try {
                   const response = await apiService.getUserLibrary(token);
                   const libraryData = await response.json();
                   setIsInLibrary(libraryData.some(item => item.game.id === parseInt(id)));
               } catch (err) {
                   console.error('Error checking library status:', err);
               }
           }
       };

       checkLibraryStatus();
   }, [id, isAuthenticated, token]);

   const handleLibraryAction = async () => {
       if (!isAuthenticated) {
           setLibraryMessage('Please log in to add games to your library');
           return;
       }
   
       setAddingToLibrary(true);
       try {
           if (isInLibrary) {
               // Remove from library
               const response = await apiService.removeFromLibrary(game.id, token);
               if (response.ok) {
                   setIsInLibrary(false);
                   setLibraryMessage('Game removed from library!');
               }
           } else {
               // Add to library
               const payload = { game: game.id };
               const response = await fetch('http://localhost:8000/api/v1/library/', {
                   method: 'POST',
                   headers: {
                       'Content-Type': 'application/json',
                       'Authorization': `Token ${token}`
                   },
                   body: JSON.stringify(payload)
               });
               
               if (response.ok) {
                   setIsInLibrary(true);
                   setLibraryMessage('Game added to library!');
               } else {
                   const data = await response.json();
                   console.log('Error data:', data);
                   setLibraryMessage(data.error || 'Failed to add to library');
               }
           }
       } catch (err) {
           console.error('Error updating library:', err);
           setLibraryMessage('Failed to update library');
       } finally {
           setAddingToLibrary(false);
       }
   };

   if (loading) {
       return (
           <div className="flex justify-center items-center min-h-screen bg-gray-900">
               <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-white"></div>
           </div>
       );
   }

   if (error || !game) {
       return (
           <div className="flex justify-center items-center min-h-screen bg-gray-900">
               <div className="text-white text-xl">
                   {error || 'Game not found'}
               </div>
           </div>
       );
   }

   return (
       <div className="min-h-screen bg-gray-900 py-8">
           <div className="max-w-6xl mx-auto px-4">
               <div className="bg-gray-800 rounded-lg overflow-hidden shadow-xl">
                   <img
                       src={game.image_url || '/placeholder-game.jpg'}
                       alt={game.title}
                       className="w-full h-96 object-cover"
                   />

                   <div className="p-6">
                       <div className="flex justify-between items-start">
                           <div>
                               <h1 className="text-4xl font-bold text-white mb-2">
                                   {game.title}
                               </h1>
                               <p className="text-gray-400 text-lg mb-4">
                                   {game.genre}
                               </p>
                           </div>
                           <div className="text-right">
                               <div className="text-3xl text-green-500 font-bold">
                                   ${game.price}
                               </div>
                               {game.sale && (
                                   <span className="bg-red-500 text-white px-3 py-1 rounded text-sm ml-2">
                                       On Sale!
                                   </span>
                               )}
                           </div>
                       </div>

                       <div className="mt-6">
                           <h2 className="text-xl font-bold text-white mb-2">
                               About This Game
                           </h2>
                           <p className="text-gray-300 leading-relaxed">
                               {game.description}
                           </p>
                       </div>

                       <div className="mt-8">
                           {libraryMessage && (
                               <div className={`mb-4 p-3 rounded ${
                                   libraryMessage.includes('Failed') || libraryMessage.includes('Please log in')
                                       ? 'bg-red-500'
                                       : 'bg-green-500'
                               } text-white`}>
                                   {libraryMessage}
                               </div>
                           )}
                           <div className="flex gap-4">
                               <a 
                                   href={`https://store.steampowered.com/app/${game.steam_app_id}`}
                                   target="_blank"
                                   rel="noopener noreferrer"
                                   className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
                               >
                                   View on Steam
                               </a>
                               <button 
                                   onClick={handleLibraryAction}
                                   disabled={addingToLibrary}
                                   className={`${
                                       addingToLibrary 
                                           ? 'bg-gray-400 cursor-not-allowed' 
                                           : isInLibrary
                                               ? 'bg-red-600 hover:bg-red-700'
                                               : 'bg-green-600 hover:bg-green-700'
                                   } text-white px-6 py-2 rounded`}
                               >
                                   {addingToLibrary 
                                       ? 'Processing...' 
                                       : isInLibrary 
                                           ? 'Remove from Library' 
                                           : 'Add to Library'}
                               </button>
                           </div>
                       </div>
                   </div>
               </div>
           </div>
       </div>
   );
};

export default GameDetailsPage;