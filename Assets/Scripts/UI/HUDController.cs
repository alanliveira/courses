using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class HUDController : MonoBehaviour {

    [Header("Barra de status")]
    public GameObject painelCharacter;
    public Image imageCharacter;
    public Text nomeCharacter;
    public Scrollbar vidaCharacter;
    public Scrollbar estaminaCharacter;

    [Header("Painel de interação")]
    public GameObject painelInterable;
    public Text actionInterable;
    public Image actionButtonInterable;

    [Header("Painel de Dialogo")]
    public GameObject painelDialog;
    public Text titleDialog;
    public Text descDialog;
    public Image actionButtonDialog;

    [Header("Painel de missão")]
    public GameObject painelMission;
    public Image imageMission;
    public Text titleMission;
    public Text menssageMission;
    public float tempoVisualizacao = 10f;

    [Header("Iventário")]
    public GameObject painelIventerio;

    private GameData gd;

    private void Awake()
    {
        gd = GameObject.Find("GameData").GetComponent<GameData>();
    }

    private void LateUpdate()
    {
        characterStatus();
    }
    
    /// <summary>
    /// Função que verifica a visibilidade do painel
    /// </summary>
    /// <returns></returns>
    public bool interableVisible()
    {
        return painelInterable.activeSelf;
    }

    /// <summary>
    /// Função que controla a visibilidade do painel de interação
    /// </summary>
    /// <param name="enable">Estado da visibilidade</param>
    public void interable(bool enable = false)
    {
        painelInterable.SetActive(enable);
    }

    /// <summary>
    /// Função que alteração o nome da ação da interação
    /// </summary>
    /// <param name="action">O nome que deseja alterar<param>
    public void interable(string action)
    {
        actionInterable.text = action;
    }

    /// <summary>
    /// Função que controla a visibilidade do painel de interação e define os paramentros da ação
    /// </summary>
    /// <param name="enable">visibilidade do painel</param>
    /// <param name="action">O nome que deseja alterar</param>
    /// <param name="KeyButtonAction">tecla que será apertada</param>
    public void interable(bool enable, string action, Sprite KeyButtonAction)
    {
        interable(action);
        this.actionButtonInterable.sprite = KeyButtonAction;
        interable(enable);
    }

    /// <summary>
    /// Função que mostra os dados atual do character controlável
    /// </summary>
    private void characterStatus()
    {
        PlayerTable p = gd.characterAtual().player;

        imageCharacter.sprite = p.Avatar;
        nomeCharacter.text = p.Nome;
        vidaCharacter.size = p.VidaAtual / p.VidaMax;
        estaminaCharacter.size = p.EnergiaAtual / p.EnergiaMax;
    }

    /// <summary>
    /// Função que retorna a visibilidade do painel de dialogos
    /// </summary>
    /// <returns></returns>
    public bool dialogVisible()
    {
        return painelDialog.activeSelf;
    }

    /// <summary>
    /// Função que altera a visibilidade do painel de dialogos
    /// </summary>
    /// <param name="enable">Estado da visibilidade</param>
    public void dialog(bool enable)
    {
        painelDialog.SetActive(enable);
    }

    /// <summary>
    /// Função que define o título e descrição do painel de dialogos
    /// </summary>
    /// <param name="titleDialog">Altera o título do dialogo</param>
    /// <param name="descDialog">Altera a descrição do diálogo</param>
    public void dialog(string titleDialog, string descDialog)
    {
        this.titleDialog.text = titleDialog;
        this.descDialog.text = descDialog;
    }

    /// <summary>
    /// Função que define o título e descrição do painel de dialogos
    /// </summary>
    /// <param name="enable">Estado da visibilidade</param>
    /// <param name="titleDialog">Altera o título do painel de dialogo</param>
    /// <param name="descDialog">Altera a descrição do painel de dialogo</param>
    /// <param name="actionButtonDialog">Altera o icone do botão do painel de dialogo</param>
    public void dialog(bool enable, string titleDialog, string descDialog, Sprite actionButtonDialog) 
    {
        dialog(titleDialog, descDialog);
        //this.actionButtonDialog.sprite = actionButtonDialog;

        dialog(enable);
    }

    public void mission(bool enable)
    {
        painelMission.SetActive(enable);
    }

    public void mission(float tempoVisualizacao)
    {
        this.tempoVisualizacao = tempoVisualizacao;
        StartCoroutine(VisualizationMission(tempoVisualizacao));
    }

    public void mission(Sprite imageMission, string titleMission, string menssageMission)
    {
        this.imageMission.sprite = imageMission;
        this.titleMission.text = titleMission;
        this.menssageMission.text = menssageMission;
    }

    public void mission(bool enable, Sprite imageMission, string titleMission, string menssageMission, float tempoVisualizacao)
    {
        mission(enable);
        mission(imageMission, titleMission, menssageMission);
        mission(tempoVisualizacao);
    }

    IEnumerator VisualizationMission(float tempo)
    {
        yield return new WaitForSeconds(tempo);
        mission(false);
    }

    public bool inventoryActive()
    {
        return painelIventerio.activeSelf;
    }

    public void inventory(bool enable)
    {
        painelIventerio.SetActive(enable);
    }
}
