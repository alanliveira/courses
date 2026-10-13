let isRunning = false;

self.onmessage = function (event) {
  if (isRunning) return;

  isRunning = true;

  const state = event.data;
  const { activeTask, secondsRemaining } = state;

  const endDate = activeTask.startDate + secondsRemaining * 1_000;
  const now = Date.now();
  let countDownSeconds = Math.floor((endDate - now) / 1_000);

  function tick() {
    self.postMessage(countDownSeconds);

    const now = Date.now();
    countDownSeconds = Math.floor((endDate - now) / 1_000);

    setTimeout(tick, 1_000);
  }

  tick();
};
