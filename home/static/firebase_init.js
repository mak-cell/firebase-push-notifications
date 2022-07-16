
const firebaseConfig = {
    apiKey: "AIzaSyBJeuQ3ZAjQlE77daP92qNVKgdt0EhQXmM",
    authDomain: "bazarside-mak.firebaseapp.com",
    projectId: "bazarside-mak",
    storageBucket: "bazarside-mak.appspot.com",
    messagingSenderId: "559823649981",
    appId: "1:559823649981:web:258ed7771ca85a3bdb4bd4",
    measurementId: "G-L7M9P9L1VS"
  };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    firebase.analytics();
    const messaging = firebase.messaging();
    console.log(messaging.getToken())
    messaging.getToken({ vapidKey: 'BEb9aXznQAxK1TNlcg8yGjeLvaogazQQKgXv97mblJED1yYdn_vGhbrYsKLRpqYPOsz2qmkOiWqGKEjRaNdRF0k' }).then((currentToken) => {
      if (currentToken) {
        console.log("token: ", currentToken);
        
      if (!(isTokenSentToServer()))
      {
        sendTokenToServer(currentToken);
      }
      } else {
        console.log('No registration token available. Request permission to generate one.');
      }
    }).catch((err) => {
      console.log('An error occurred while retrieving token. ', err);
    });
    
  
    messaging
     .requestPermission()
     .then(function () {
       console.log("Notification permission granted....");
       return messaging.getToken()
     })
     .catch(function (err) {
     console.log("Unable to get permission to notify.", err);
   });
  
  
    messaging.onMessage((payload) => {
    console.log('Message received. ', payload);
   
  });

  
  function isTokenSentToServer() {
    return window.localStorage.getItem('sentToServer') === '1';
  }

  function setTokenSentToServer(sent) {
    window.localStorage.setItem('sentToServer', sent ? '1' : '0');
  }
  
  function sendTokenToServer(currentToken) {
    console.log('Sending token to server...');
    console.log('Cheking incognito...');
    if (!isTokenSentToServer()) {
      ifIncognito(false, ()=>{ 
      console.log('Sending token to server...');
      
      let url = "/send_device_id/"
      $.ajax({
        url: url,
        type: 'POST',
      data: {
        "token":currentToken,
      },
      enctype: 'multipart/form-data',
      success: function () {
          console.log("token sent to server...");
          setTokenSentToServer(true);
      },
      error: function (data) {
        console.log("token send faliure");
      }
    });
  });
    } 
    else {
      console.log('Token already sent to server so won\'t send it again ' +
          'unless it changes');
    }
  }


  function deleteToken() {
    // Delete registration token.
    messaging.getToken().then((currentToken) => {
      messaging.deleteToken(currentToken).then(() => {
        console.log('Token deleted.');
        setTokenSentToServer(false);
        // Once token is deleted update UI.
      }).catch((err) => {
        console.log('Unable to delete token. ', err);
      });
    }).catch((err) => {
      console.log('Error retrieving registration token. ', err);
    });
  }

  function ifIncognito(incog,func){
    var fs = window.RequestFileSystem || window.webkitRequestFileSystem;
    if (!fs)  console.log("checking incognito failed");
    else {
        if(incog) fs(window.TEMPORARY, 100, ()=>{}, func);
        else      fs(window.TEMPORARY, 100, func, ()=>{});
    }
} 
  