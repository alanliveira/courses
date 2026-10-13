using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LocalPosition : MonoBehaviour {

	public bool[] ocupado;
	public Transform[] referencesPosition;

	void Start() {
		referencesPosition = GetComponentsInChildren<Transform>();
		ocupado = new bool[referencesPosition.Length];
		for (int i = 0; i <= ocupado.Length; i++) {
			ocupado [i] = false;
		}
	}
		
}
