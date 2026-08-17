using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "NPC", menuName = "Data/Caracter/NPC", order = 3)]
public class NpcTable : ScriptableObject {

    [Header("propriedades")]
    [SerializeField]
    private string nome;
    [SerializeField] private string classe;

    [Header("Deslocamento")]
    [SerializeField]
    private float speed = 3f;
    [SerializeField] private float speedMax = 10f;

    public string Nome
    {
        get
        {
            return nome;
        }

        set
        {
            nome = value;
        }
    }

    public string Classe
    {
        get
        {
            return classe;
        }

        set
        {
            classe = value;
        }
    }

    public float Speed
    {
        get
        {
            return speed;
        }

        set
        {
            speed = value;
        }
    }

    public float SpeedMax
    {
        get
        {
            return speedMax;
        }

        set
        {
            speedMax = value;
        }
    }
}
