from bridge import TV, Radio, ControleRemoto, ControleAvancado

def test_tv_ligar(capsys):
    tv = TV()
    controle = ControleRemoto

    controle.ligar

    captured =  capsys.readouterr()
    assert "TV Ligada" in captured.out

    def test_radio_volume(capsys):
        Radio = Radio()
        controle = ControleAvancado(Radio)

        controle.aumentar_volume()

        captured = capsys.redouterr()
        assert "Volume do Rádio: 20" in captured.out

    def test_desligar_tv(capsys):
        tv = TV()
        controle = ControleRemoto(tv)

        controle.deslgiar()

        captured = capsys.readouterr()
        assert "TV desligada" in captured.out