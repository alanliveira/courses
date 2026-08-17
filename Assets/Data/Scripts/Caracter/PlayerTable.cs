using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName ="Character",menuName ="Data/Character/Player",order =2)]
public class PlayerTable : ScriptableObject {
    [Header("propriedades")]
    [SerializeField] private string nome;
    [SerializeField] private Sprite avatar;
    [SerializeField] private string classe;

    [Header("Deslocamento")]
    [SerializeField] private float speed = 3f;
    [SerializeField] private float speedMax = 10f;
    [SerializeField] private float turnSpeed = 10;
    [SerializeField] private float jump = 10;

    [Header("Status")]
    [SerializeField] private float vidaMax;
    [SerializeField] private float vidaAtual;
    [SerializeField] private float energiaMax;
    [SerializeField] private float energiaAtual;

    [Header("Batalha")]
    [SerializeField] private float ataque = 10;
    [SerializeField] private float defesa = 10;

    [Header("Equipamentos")]
    [SerializeField] private EquipamentosTable equipamento;

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

    public float VidaMax
    {
        get
        {
            return vidaMax;
        }

        set
        {
            vidaMax = value;
        }
    }

    public float VidaAtual
    {
        get
        {
            return vidaAtual;
        }

        set
        {
            vidaAtual = value;
        }
    }

    public float EnergiaMax
    {
        get
        {
            return energiaMax;
        }

        set
        {
            energiaMax = value;
        }
    }

    public float EnergiaAtual
    {
        get
        {
            return energiaAtual;
        }

        set
        {
            energiaAtual = value;
        }
    }

    public float Ataque
    {
        get
        {
            return ataque;
        }

        set
        {
            ataque = value;
        }
    }

    public float Defesa
    {
        get
        {
            return defesa;
        }

        set
        {
            defesa = value;
        }
    }

    public EquipamentosTable Equipamento
    {
        get
        {
            return equipamento;
        }

        set
        {
            equipamento = value;
        }
    }

    public float TurnSpeed
    {
        get
        {
            return turnSpeed;
        }

        set
        {
            turnSpeed = value;
        }
    }

    public float Jump
    {
        get
        {
            return jump;
        }

        set
        {
            jump = value;
        }
    }

    public Sprite Avatar
    {
        get
        {
            return avatar;
        }

        set
        {
            avatar = value;
        }
    }
}
