const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");

const BOT_MSGS =""
/*
// Icons made by Freepik from www.flaticon.com
const BOT_IMG = ""
//"https://tint.edu.in/images/tict_logo_new_2019.png";
const PERSON_IMG = ""
//"static/student.png";
const BOT_NAME = "GURUPRANAM";
const PERSON_NAME = "You";

msgerForm.addEventListener("submit", event => {
  event.preventDefault();

  const msgText = msgerInput.value;
  if (!msgText) return;

  appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
  msgerInput.value = "";
  msgerInput.focus();

  botResponse(msgText);
});
*/
function appendMessage(name, img, side, text) {
  //   Simple solution for small apps
  const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-img" style="background-image: url(${img})"></div>

      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
      </div>
    </div>
  `;

  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
}

function botResponse(mesg) {
  const r = random(0, BOT_MSGS.length - 1);
  (async () => {
let response = await fetch('/chat',{
  method: 'POST',
  body: mesg
});

let text = await response.text(); // read response body as text

  const msgText1 = text.split(" 0 ");
  //const delay = msgText.split(" ").length * 100;
  appendMessage(BOT_NAME, BOT_IMG, "left", msgText1[0]);
  if(msgText1[1]){
  const delay = msgText1[0].split(" ").length * 200;
  setTimeout(() => {
  appendMessage(BOT_NAME, BOT_IMG, "left", msgText1[1]);
  },delay);}
  })()
}

// Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}

function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}

function random(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}
