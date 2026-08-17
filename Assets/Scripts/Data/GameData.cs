using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameData : MonoBehaviour {
    
    public List<CharacterController> players;

    public int indexPlayer = 1;
    public GameObject positionCharacters;

	public LocalPosition targetPosition;

    private void Start()
    {
        mudarPlayer();
    }

	private void gerenciarPosicoes() {
		GameObject g = Instantiate(positionCharacters, players[indexPlayer].transform, false) as GameObject;
		targetPosition = g.GetComponent<LocalPosition>();
	}

    public void mudarPlayer()
    {
        for (int i = 0; i <= players.Count-1; i++)
        {
            players[i].controllerPlayer = false;
        }
        players[indexPlayer].controllerPlayer = true;

		//gerenciarPosicoes ();
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.KeypadPlus))
        {
            if(indexPlayer >= players.Count-1)
            {
                indexPlayer = 0;
            } else
            {
                indexPlayer++;
            }

            mudarPlayer();
        }
    }

    //Função que retorna o character que pode ser controlado
    public CharacterController characterAtual()
    {
        for (int i = 0; i < players.Count; i++)
        {
            if (players[i].controllerPlayer) return players[i];
        }
        return null;
    }
}
