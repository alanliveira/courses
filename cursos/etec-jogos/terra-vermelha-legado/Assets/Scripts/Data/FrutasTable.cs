using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "Fruta", menuName = "Data/Item/Fruta", order = 3)]
public class FrutasTable : ScriptableObject
{
    public string nome;
    public int recuperacaoVida;
    public Sprite icon2D;
}
