using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using UnityEngine;
using UnityEditor;

[CreateAssetMenu(fileName = "dialogo", menuName = "Data/dialogo/npc", order = 3)]
public class DialogoTable : ScriptableObject {
	
	public string nome;
	[TextArea]public List<string> dialogos;
}
