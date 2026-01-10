const ROUNDS_RACING = 5;

const players = [
  {
    fullName: "Mario",
    velocity: 4,
    maneuverability: 3,
    power: 3,
  },
  {
    fullName: "Peach",
    velocity: 3,
    maneuverability: 4,
    power: 2,
  },
  {
    fullName: "Yoshi",
    velocity: 2,
    maneuverability: 4,
    power: 3,
  },
  {
    fullName: "Bowser",
    velocity: 5,
    maneuverability: 2,
    power: 5,
  },
  {
    fullName: "Luigi",
    velocity: 3,
    maneuverability: 4,
    power: 4,
  },
  {
    fullName: "Donkey Kong",
    velocity: 2,
    maneuverability: 2,
    power: 5,
  },
];

const player1 = {
  character: players[Math.floor(Math.random() * players.length)],
  points: 0,
};

const otherPlayers = players.filter(
  (player) => player.fullName !== player1.character.fullName
);

const player2 = {
  character: otherPlayers[Math.floor(Math.random() * otherPlayers.length)],
  points: 0,
};

const items = [
  { typeName: "casco", value: 1, symbol: '🐢' },
  { typeName: "bomba", value: 2, symbol: '💣' },
  { typeName: "Raio", value: 3, symbol: '⛈️' },
];

const rollDice = async () => Math.floor(Math.random() * 6) + 1;

const getRandowBlock = async () => {
  let randow = Math.random();
  let result = null;

  switch (true) {
    case randow < 0.33:
      result = "RETA";
      break;
    case randow < 0.66:
      result = "CURVA";
      break;
    default:
      result = "CONFRONTO";
      break;
  }

  return result;
};

const playRaceEngine = async () => {
  for (let round = 1; round <= ROUNDS_RACING; round++) {
    await logTitle("🏁", `Rodada ${round}`);

    const block = await getRandowBlock();
    console.log(`Bloco: ${block}`);

    if (block === "CONFRONTO") {
      console.log(
        `${player1.character.fullName} confrontou com ${player2.character.fullName}!🥊`
      );
    }

    let resultCharacter1 = await playCharacter(player1.character, block);
    let resultCharacter2 = await playCharacter(player2.character, block);

    if (block !== "CONFRONTO") {
      if (resultCharacter1.totalTestSkill > resultCharacter2.totalTestSkill) {
        console.log(`${player1.character.fullName} marcou 1 ponto!`);
        player1.points++;
      } else if (
        resultCharacter2.totalTestSkill > resultCharacter1.totalTestSkill
      ) {
        console.log(`${player2.character.fullName} marcou 1 ponto!`);
        player2.points++;
      } else {
        console.log(`Nenhum dos player fez a pontuação!`);
      }
    } else {
      const item = items[Math.floor(Math.random() * items.length)];

      if (resultCharacter1.power > resultCharacter2.power) {
        player2.character.points = player2.character.points - item.value;
        player2.character.points = player2.character.points > 0 ? 0 : player2.character.points
        
        console.log(
          `${player1.character.fullName} venceu o confronto! ${player2.character.fullName} perdeu ${item.value} por ${item.symbol}`
        );
      } else if (resultCharacter2.power > resultCharacter1.power) {
        player1.character.points = player1.character.points - item.value;
        player1.character.points = player1.character.points > 0 ? 0 : player1.character.points

        console.log(
          `${player2.character.fullName} venceu o confronto! ${player1.character.fullName} perdeu 1 ponto 🐢`
        );
      } else {
        console.log("Confronto empatado! nenhum ponto foi perdido");
      }
    }

    // console.info(`${player1.character.fullName}: ${player1.points} | ${player2.character.fullName}: ${player2.points}`)
  }
};

const logLine = async () =>
  console.log(
    "-----------------------------------------------------------------"
  );

const logTitle = async (symbol, title) => {
  await logLine();
  console.log(` ${symbol} | ${title}`);
  await logLine();
};

const playCharacter = async (character, bloco) => {
  // teste de habilidade
  const result = {
    dice: null,
    totalTestSkill: null,
    attribute: null,
    testHability: null,
    power: null,
  };

  result.dice = await rollDice();

  if (bloco === "RETA") {
    result.attribute = character.velocity;
    result.totalTestSkill = character.velocity + result.dice;
  } else if (bloco === "CURVA") {
    result.attribute = character.maneuverability;
    result.totalTestSkill = character.maneuverability + result.dice;
  } else if (bloco === "CONFRONTO") {
    result.attribute = character.power;
    result.power = character.power + result.dice;
  }

  console.log(
    `${character.fullName} 🎲 rolou o dado de ${bloco} ${result.dice} + ${
      result.attribute
    } = ${result.dice + result.attribute}`
  );

  return result;
};

const declareWinner = async () => {
  await logTitle("🏆", "Resultado final");
  console.log(`${player1.character.fullName}: ${player1.points} ponto(s)`);
  console.log(`${player2.character.fullName}: ${player2.points} ponto(s)`);
  console.log("\n");

  if (player1.points > player2.points)
    console.log(`${player1.character.fullName} venceu a corrida! Parabéns! 🏆`);
  else if (player2.points > player1.points)
    console.log(`${player2.character.fullName} venceu a corrida! Parabéns! 🏆`);
  else {
    console.log(`A corrida terminou em empate!`);
  }

  console.log("\n");
};

(async function main() {
  console.log(
    `🏁🚨 Corrida entre ${player1.character.fullName} e ${player2.character.fullName} começando ...`
  );

  await playRaceEngine();
  await declareWinner();
})();
