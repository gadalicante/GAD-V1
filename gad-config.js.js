/* ARCHIVO: gad-config.js
   UBICACIÓN: Raíz (junto a los HTML)
   DESCRIPCIÓN: Configuración centralizada de Firebase y Seguridad GAD.
*/

const firebaseConfig = {
  apiKey: "AIzaSyBu5ALRVJ5aDzuU9YIAQD_9KMgR6ZwttpU",
  authDomain: "gad-alicante-v1.firebaseapp.com",
  databaseURL: "https://gad-alicante-v1-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "gad-alicante-v1",
  storageBucket: "gad-alicante-v1.firebasestorage.app",
  messagingSenderId: "545835357966",
  appId: "1:545835357966:web:6351ec6c0d3c8e69eb695f",
  measurementId: "G-QG8KDLCWQS"
};

// Inicializar Firebase si no está activo
if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}

// Emails Autorizados (Seguridad Nivel Servidor)
const AUTHORIZED_EMAILS = ['gadalicante@gmail.com', 'copg279@gmail.com'];

// Función de verificación rápida
function verificarSesionActiva() {
    return new Promise((resolve, reject) => {
        firebase.auth().onAuthStateChanged((user) => {
            if (user && AUTHORIZED_EMAILS.includes(user.email)) {
                resolve(user);
            } else {
                reject("No autorizado");
            }
        });
    });
}