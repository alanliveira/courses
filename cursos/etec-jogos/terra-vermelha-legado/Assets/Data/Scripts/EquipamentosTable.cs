using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName ="Equipamento",menuName ="Data/Item/Equipamento",order =2)]
public class EquipamentosTable : ScriptableObject {

    public enum TipoEquipamento
    {
        lanca, estilingue, forca
    }

    [SerializeField] private string nome;
    [SerializeField] private TipoEquipamento tipo;
    [SerializeField] private float agilidade;
    [SerializeField] private float forca;
    [SerializeField] private float protecao;
    [SerializeField] private float precisao;

    public float Agilidade
    {
        get
        {
            return agilidade;
        }

        set
        {
            agilidade = value;
        }
    }

    public float Protecao
    {
        get
        {
            return protecao;
        }

        set
        {
            protecao = value;
        }
    }

    public TipoEquipamento Tipo
    {
        get
        {
            return tipo;
        }

        set
        {
            tipo = value;
        }
    }

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
}
