from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
size = 1

# -------------------- LA CREATION DES OBJETS --------------------

def creer_bloc_herbe(position):
    Entity(
        model='cube',
        color=color.rgba(255, 255, 255, 0),
        position=position,
        scale=size,
        collider='box',
        visible=True
    )
    facesherbe = [
        {'pos': (0, 0, 0.5), 'rot': (0, 0, 0), 'tex': 'textures/Herbe/bloc_cote.png'},
        {'pos': (0, 0, -0.5), 'rot': (0, 180, 0), 'tex': 'textures/Herbe/bloc_cote.png'},
        {'pos': (0.5, 0, 0), 'rot': (0, 90, 0), 'tex': 'textures/Herbe/bloc_cote.png'},
        {'pos': (-0.5, 0, 0), 'rot': (0, -90, 0), 'tex': 'textures/Herbe/bloc_cote.png'},
        {'pos': (0, 0.5, 0), 'rot': (90, 0, 0), 'tex': 'textures/Herbe/bloc_dessus.png'},
        {'pos': (0, -0.5, 0), 'rot': (-90, 0, 0), 'tex': 'textures/Herbe/bloc_bas.png'},
    ]
    for f in facesherbe:
        Entity(
            model='quad',
            texture=f['tex'],
            position=Vec3(*f['pos']) + position,
            rotation=f['rot'],
            scale=(size, size),
            double_sided=True,
            parent=scene
        )

def creer_bloc_chemin(position):
    Entity(
        model='cube',
        color=color.rgba(255, 255, 255, 0),
        position=position,
        scale=size,
        collider='box',
        visible=True
    )
    faceschemin = [
        {'pos': (0, 0, 0.5), 'rot': (0, 0, 0), 'tex': 'textures/Chemin/bloc_cote.png'},
        {'pos': (0, 0, -0.5), 'rot': (0, 180, 0), 'tex': 'textures/Chemin/bloc_cote.png'},
        {'pos': (0.5, 0, 0), 'rot': (0, 90, 0), 'tex': 'textures/Chemin/bloc_cote.png'},
        {'pos': (-0.5, 0, 0), 'rot': (0, -90, 0), 'tex': 'textures/Chemin/bloc_cote.png'},
        {'pos': (0, 0.435, 0), 'rot': (90, 0, 0), 'tex': 'textures/Chemin/bloc_dessus.png'},
        {'pos': (0, -0.5, 0), 'rot': (-90, 0, 0), 'tex': 'textures/Chemin/bloc_bas.png'},
    ]
    for f in faceschemin:
        Entity(
            model='quad',
            texture=f['tex'],
            position=Vec3(*f['pos']) + position,
            rotation=f['rot'],
            scale=(size, size),
            double_sided=True,
            parent=scene,
        )

def creer_bloc_tronc(position):
    facestronc = [
        {'pos': (0, 0, 0.5), 'rot': (0, 0, 0), 'tex': 'textures/Arbre/bloc_cote.png'},
        {'pos': (0, 0, -0.5), 'rot': (0, 180, 0), 'tex': 'textures/Arbre/bloc_cote.png'},
        {'pos': (0.5, 0, 0), 'rot': (0, 90, 0), 'tex': 'textures/Arbre/bloc_cote.png'},
        {'pos': (-0.5, 0, 0), 'rot': (0, -90, 0), 'tex': 'textures/Arbre/bloc_cote.png'},
        {'pos': (0, 0.5, 0), 'rot': (90, 0, 0), 'tex': 'textures/Arbre/bloc_dessus_bas.png'},
        {'pos': (0, -0.5, 0), 'rot': (-90, 0, 0), 'tex': 'textures/Arbre/bloc_dessus_bas.png'},
    ]
    for f in facestronc:
        Entity(
            model='quad',
            texture=f['tex'],
            position=Vec3(*f['pos']) + position,
            rotation=f['rot'],
            scale=(size, size),
            double_sided=True,
            parent=scene,
            collider='box'
        )

def creer_bloc_plante(position, rotation_y=45):
    bloc = Entity(position=position, rotation_y=rotation_y)
    facesplante = [
        {'pos': (0, 0, 0), 'rot': (0, 0, 0), 'tex': 'textures/Plantes/bloc_cote.png'},
        {'pos': (0, 0, 0), 'rot': (0, 90, 0), 'tex': 'textures/Plantes/bloc_cote.png'},
    ]
    for f in facesplante:
        Entity(
            model='quad',
            texture=f['tex'],
            position=Vec3(*f['pos']),
            rotation=Vec3(*f['rot']),
            scale=(size, size),
            double_sided=True,
            parent=bloc
        )

def creer_bloc_fleur_rouge(position, rotation_y=45):
    bloc = Entity(position=position, rotation_y=rotation_y)
    facesfleurrouge = [
        {'pos': (0, 0, 0.5), 'rot': (0, 0, 0), 'tex': 'textures/Fleurs/bloc_fleur_rouge.png'},
        {'pos': (0, 0, 0.5), 'rot': (0, 90, 0), 'tex': 'textures/Fleurs/bloc_fleur_rouge.png'},
    ]
    for f in facesfleurrouge:
        Entity(
            model='quad',
            texture=f['tex'],
            position=Vec3(*f['pos']),
            rotation=Vec3(*f['rot']),
            scale=(size, size),
            double_sided=True,
            parent=bloc
        )

def creer_bloc_fleur_jaune(position, rotation_y=45):
    bloc = Entity(position=position, rotation_y=rotation_y)
    facesfleurjaune = [
        {'pos': (0, 0, 0.5), 'rot': (0, 0, 0), 'tex': 'textures/Fleurs/bloc_fleur_jaune.png'},
        {'pos': (0, 0, 0.5), 'rot': (0, 90, 0), 'tex': 'textures/Fleurs/bloc_fleur_jaune.png'},
    ]
    for f in facesfleurjaune:
        Entity(
            model='quad',
            texture=f['tex'],
            position=Vec3(*f['pos']),
            rotation=Vec3(*f['rot']),
            scale=(size, size),
            double_sided=True,
            parent=bloc
        )

def creer_bloc_barriere(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/fence.obj',         
        texture='textures/oak_planks.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box"
    )
    return bloc

def creer_bloc_barriere_angle(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/fenceangle.obj',         
        texture='textures/oak_planks.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box"
    )
    return bloc

def creer_bloc_portillon(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/fencegate.obj',         
        texture='textures/oak_planks.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box"
    )
    return bloc

def creer_bloc_pillier_foncé(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/fencebody.obj',         
        texture='textures/spruce_planks.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box"
    )
    return bloc

def creer_bloc_barrière_foncé(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/fencepostdemi.obj',         
        texture='textures/spruce_planks.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box",
        scale=taille
    )
    return bloc

def creer_bloc_lanterne(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/lantern.obj',         
        texture='textures/lantern.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box"
    )
    return bloc


def creer_bloc_feuilles(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/azalealeaves.obj',         
        texture='textures/azalea_leaves.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box",
        scale=taille
    )
    return bloc

def creer_bloc_feuille_superposition(position, taille=1):
    bloc = Entity(
        model="cube",
        color=color.rgb(245, 245, 245),
        position=position,
        collider="box",
        scale=taille,
        visible=False
    )

def creer_cochon(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/pig.obj',         
        texture='textures/pig.png',
        rotation_y=rotation_y,    
        position=position,
    )
    return bloc

def creer_villageois_fermier(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/villagerfarmer.obj',         
        texture='textures/villagerfarmer.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box"
    )
    return bloc

def creer_perroquet_rouge(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/parrot.obj',         
        texture='textures/parrotred.png',
        rotation_y=rotation_y,    
        position=position,
        double_sided=True
    )
    return bloc

def creer_perroquet_bleu(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/parrot.obj',         
        texture='textures/parrotblue.png',
        rotation_y=rotation_y,    
        position=position,
        double_sided=True
    )
    return bloc

def creer_perroquet_gris(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/parrot.obj',
        texture='textures/parrotyellow.png',
        roration_y=rotation_y,
        position=position,
        double_sided=True
    )
    return bloc

def creer_poulet(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/chicken.obj',         
        texture='textures/chicken.png',
        rotation_y=rotation_y,    
        position=position,
        double_sided=True,
        collider="box"
    )
    return bloc

def creer_golem_fer(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/irongolem.obj',         
        texture='textures/irongolem.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box"
    )
    return bloc

def creer_bloc_ruche(position):
    facesruche = [
        {'pos': (0, 0, 0.5), 'rot': (0, 0, 0), 'tex': 'textures/Ruche/bee_nest_side.png'},
        {'pos': (0, 0, -0.5), 'rot': (0, 180, 0), 'tex': 'textures/Ruche/bee_nest_side.png'},
        {'pos': (0.5, 0, 0), 'rot': (0, 90, 0), 'tex': 'textures/Ruche/bee_nest_front.png'},
        {'pos': (-0.5, 0, 0), 'rot': (0, -90, 0), 'tex': 'textures/Ruche/bee_nest_front.png'},
        {'pos': (0, 0.5, 0), 'rot': (90, 0, 0), 'tex': 'textures/Ruche/bee_nest_top.png'},
        {'pos': (0, -0.5, 0), 'rot': (-90, 0, 0), 'tex': 'textures/Ruche/bee_nest_bottom.png'},
    ]
    for f in facesruche:
        Entity(
            model='quad',
            texture=f['tex'],
            position=Vec3(*f['pos']) + position,
            rotation=f['rot'],
            scale=(size, size),
            double_sided=True,
            parent=scene,
            collider='box'
        )

def creer_abeille(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/bee.obj',
        texture='textures/bee.png',
        rotation_y=rotation_y,
        position=position,
        collider='box'
    )
    return bloc

def creer_loup(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/wolf.obj',
        texture='textures/wolf.png',
        rotation_y=rotation_y,
        position=position,
        double_sided=True,
        collider='box'
    )
    return bloc

def creer_lapin(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/rabbit.obj',
        texture='textures/rabbit.png',
        rotation_y=rotation_y,
        position=position,
        double_sided=True,
        collider='box'
    )
    return bloc

def creer_bloc_pierre_taillée(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/stone_bricks.obj',
        texture='textures/stone_bricks.png',
        rotation_y=rotation_y,
        position=position,
        double_sided=True,
        collider='box'
    )
    return bloc

def creer_bloc_pierre_cobblestone(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/cobblestone.obj',
        texture='textures/cobblestone.png',
        rotation_y=rotation_y,
        position=position,
        double_sided=True,
        collider='box'
    )
    return bloc

def creer_bloc_planche_chêne(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/oak_planks.obj',
        texture='textures/oak_planks.png',
        rotation_y=rotation_y,
        position=position,
        double_sided=True,
        collider='box'
    )
    return bloc

def creer_bloc_pierre_lisse(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/smooth_stone.obj',
        texture='textures/smooth_stone.png',
        rotation_y=rotation_y,
        position=position,
        double_sided=True,
        collider='box'
    )
    return bloc

def creer_bloc_escalier_cobblestone(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/stairs.obj',
        texture='textures/cobblestone.png',
        rotation_y=rotation_y,
        position=position,
        double_sided=True,
        collider='box'
    )
    return bloc

def creer_bloc_dalle_pierre_taillée(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/stone_bricks.obj',
        texture='textures/slab.png',
        rotation_y=rotation_y,
        position=position,
        double_sided=True,
        collider='box'
    )
    return bloc

def creer_bloc_pillier_chene(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/fencebody.obj',         
        texture='textures/oak_planks.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box"
    )
    return bloc

def creer_bloc_barrière_chene(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/fencepostdemi.obj',         
        texture='textures/oak_planks.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box",
        scale=taille
    )
    return bloc

def creer_bloc_barrière_chene_milieux(position, rotation_y=0, taille=1):
    bloc = Entity(
        model='models/fence-side.obj',         
        texture='textures/oak_planks.png',
        rotation_y=rotation_y,    
        position=position,
        collider="box",
        scale=taille
    )
    return bloc

# -------------------- LA POSE DES OBJETS --------------------

# --- CHUNK 1 ---

# --- HERBE 1 ---

for x in range(25, 155, 10):
    for z in range(-15, 0, 1):
            creer_bloc_herbe(position=Vec3(x/10, 0, z))

# --- HERBE 2 ---

for x in range(-135, -5, 10):
    for z in range(-15, 0, 1):
        creer_bloc_herbe(position=Vec3(x/10, 0, z))

# --- HERBE 3 ---

for x in range(-135, 155, 10):
    for z in range(2, 7, 1):
        creer_bloc_herbe(position=Vec3(x/10, 0, z))    

# --- CHEMIN 1 ---

for x in range(-135, 155, 10):
    for z in range(0, 2, 1):
            creer_bloc_chemin(position=Vec3(x/10, 0, z))    

# --- CHEMIN 2 ---

for x in range(-5, 25, 10):
    for z in range(-15, 0, 1):
        creer_bloc_chemin(position=Vec3(x/10, 0, z))

# --- PIERRE 1 ---

for x in range(-135, -15, 10):
    creer_bloc_pierre_cobblestone(position=Vec3(x/10, 0.5, -11))

# --- PIERRE 2 ---

for x in range(-135, -5, 10):
    creer_bloc_pierre_cobblestone(position=Vec3(x/10, 0.5, -10))

# --- PIERRE 3 ---

for x in range(35, 155, 10):
    creer_bloc_pierre_cobblestone(position=Vec3(x/10, 0.5, -11))

# --- PIERRE 4 ---

for x in range(25, 155, 10):
    creer_bloc_pierre_cobblestone(position=Vec3(x/10, 0.5, -10))

# --- PIERRE 5 ---

for x in range(-135, -5, 10):
    creer_bloc_pierre_cobblestone(position=Vec3(x/10, 0.5, -15))

# --- PIERRE 6 ---

for x in range(-135, -15, 10):
    for z in range(-15, -13):
        creer_bloc_pierre_cobblestone(position=Vec3(x/10, 0.5, -14))

# --- PIERRE 7 ---

for x in range(25, 155, 10):
    creer_bloc_pierre_cobblestone(position=Vec3(x/10, 0.5, -15))

# --- PIERRE 8 ---

for x in range(35, 155, 10):
        creer_bloc_pierre_cobblestone(position=Vec3(x/10, 0.5, -14))

# --- PLANCHES CHENE 1 ---

for x in range(-135, -25, 10):
    for z in range(-13, -11):
        creer_bloc_planche_chêne(position=Vec3(x/10, 0.5, z))

# --- PLANCHES CHENE 2 ---

for x in range(45, 155, 10):
    for z in range(-13, -11):
        creer_bloc_planche_chêne(position=Vec3(x/10, 0.5, z))

# --- PILLIER BARRIERE CHENE 1 ---

for y in range(15, 55, 10):
    creer_bloc_pillier_chene(position=Vec3(2.5, y/10, -15))

# --- PILLIER BARRIERE CHENE 2 ---

for y in range(15, 55, 10):
    creer_bloc_pillier_chene(position=Vec3(-1.5, y/10, -15))

# --- PILLIER BARRIERE CHENE 3 ---

for y in range(15, 55, 10):
    creer_bloc_pillier_chene(position=Vec3(2.5, y/10, -10))

# --- PILLIER BARRIERE CHENE 4 ---

for y in range(15, 55, 10):
    creer_bloc_pillier_chene(position=Vec3(-1.5, y/10, -10))

# --- PIERRE LISSE 1 ---

for x in range(-105, -55, 10):
    for z in range(-15, -9, 5):
        for y in range(15, 45,  10):
            creer_bloc_pierre_lisse(position=Vec3(x/10, y/10, z))

for x in range(75, 125, 10):
    for z in range(-15, -9, 5):
        for y in range(15, 45, 10):
            creer_bloc_pierre_lisse(position=Vec3(x/10, y/10, z))

# --- PIERRE TAILLEE 1 ---

for y in range(15, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(-5.5, y/10, -15))

for y in range(15, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(6.5, y/10, -15))

for y in range(15, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(-5.5, y/10, -10))

for y in range(15, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(6.5, y/10, -10))

# --- PIERRE TAILLEE 2 ---

for y in range(15, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(-3.5, y/10, -15))

for y in range(15, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(4.5, y/10, -15))

for y in range(15, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(-3.5, y/10, -10))

for y in range(15, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(4.5, y/10, -10))

# PIERRE TAILLEE 3 ---

for y in range(25, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(-2.5, y/10, -15))

for y in range(25, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(-2.5, y/10, -10))

for y in range(25, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(3.5, y/10, -15))

for y in range(25, 55, 10):
    creer_bloc_pierre_taillée(position=Vec3(3.5, y/10, -10))
# --- ---

def creer_arbre(xchoisi, ychoisi, zchoisi):
    creer_bloc_tronc(position=Vec3(xchoisi, ychoisi, zchoisi))
    creer_bloc_tronc(position=Vec3(xchoisi, ychoisi + 1, zchoisi))
    creer_bloc_tronc(position=Vec3(xchoisi, ychoisi + 2, zchoisi))
    creer_bloc_tronc(position=Vec3(xchoisi, ychoisi + 3, zchoisi))
    creer_bloc_tronc(position=Vec3(xchoisi, ychoisi + 4, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 5, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi + 1, ychoisi + 4, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi + 1, ychoisi + 4, zchoisi + 1))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 4, zchoisi + 1))
    creer_bloc_feuilles(position=Vec3(xchoisi - 1, ychoisi + 4, zchoisi + 1))
    creer_bloc_feuilles(position=Vec3(xchoisi - 1, ychoisi + 4, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi - 1, ychoisi + 4, zchoisi + 1))
    creer_bloc_feuilles(position=Vec3(xchoisi - 1, ychoisi + 4, zchoisi - 1))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 4, zchoisi - 1))
    creer_bloc_feuilles(position=Vec3(xchoisi + 1, ychoisi + 4, zchoisi - 1))
    creer_bloc_feuilles(position=Vec3(xchoisi + 1, ychoisi + 3, zchoisi + 1))
    creer_bloc_feuilles(position=Vec3(xchoisi - 1, ychoisi + 3, zchoisi + 1))
    creer_bloc_feuilles(position=Vec3(xchoisi - 1, ychoisi + 3, zchoisi - 1))
    creer_bloc_feuilles(position=Vec3(xchoisi + 1, ychoisi + 3, zchoisi - 1))
    creer_bloc_feuilles(position=Vec3(xchoisi + 1, ychoisi + 3, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi + 1, ychoisi + 2, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 3, zchoisi + 1))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 2, zchoisi + 1))
    creer_bloc_feuilles(position=Vec3(xchoisi - 1, ychoisi + 3, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi - 1, ychoisi + 2, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 3, zchoisi - 1))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 2, zchoisi - 1))
    creer_bloc_feuilles(position=Vec3(xchoisi + 2, ychoisi + 3, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi + 2, ychoisi + 2, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 3, zchoisi + 2))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 2, zchoisi + 2))
    creer_bloc_feuilles(position=Vec3(xchoisi - 2, ychoisi + 3, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi - 2, ychoisi + 2, zchoisi))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 3, zchoisi - 2))
    creer_bloc_feuilles(position=Vec3(xchoisi, ychoisi + 2, zchoisi - 2))

# --- ARBRES ---

creer_arbre(-2.5, 1, 3)
creer_arbre(-4.5, 1, -6)

# --- PLANTES ---

creer_bloc_plante(position=Vec3(-1.5, 1, 2))
creer_bloc_plante(position=Vec3(-0.85, 1, 2.2))
creer_bloc_plante(position=Vec3(-0.85, 1, 3.2))
creer_bloc_plante(position=Vec3(-1.5, 1, 3))
creer_bloc_plante(position=Vec3(-2.5, 1, 4))
creer_bloc_plante(position=Vec3(-0.5, 1, 5))
creer_bloc_plante(position=Vec3(-2.5, 1, -1))
creer_bloc_plante(position=Vec3(-1.5, 1, -2))
creer_bloc_plante(position=Vec3(4.5, 1, 3))
creer_bloc_plante(position=Vec3(4.5, 1, -2))
creer_bloc_plante(position=Vec3(-4.5, 1, 4))
creer_bloc_plante(position=Vec3(-4.5, 1, 5))
creer_bloc_plante(position=Vec3(-5.5, 1, 4))
creer_bloc_plante(position=Vec3(-5.5, 1, 5))
creer_bloc_plante(position=Vec3(-5.5, 1, 2))
creer_bloc_plante(position=Vec3(-3.5, 1, 2))

# --- FLEURS ROUGES ---

creer_bloc_fleur_rouge(position=Vec3(-3.75, 1, 2.75))
creer_bloc_fleur_rouge(position=Vec3(-1.5, 1, 3.75))
creer_bloc_fleur_rouge(position=Vec3(-2.75, 1, 4.75))
creer_bloc_fleur_rouge(position=Vec3(-3.75, 1, 4.75))
creer_bloc_fleur_rouge(position=Vec3(-0.5, 1, 1.75))
creer_bloc_fleur_rouge(position=Vec3(-0.5, 1, 3.75))
creer_bloc_fleur_rouge(position=Vec3(-3.75, 1, -2.5))
creer_bloc_fleur_rouge(position=Vec3(-2.75, 1, -2.5))
creer_bloc_fleur_rouge(position=Vec3(4.15, 1, 3.5))
creer_bloc_fleur_rouge(position=Vec3(4.15, 1, 4.5))

creer_bloc_fleur_rouge(position=Vec3(-4.75, 1, 1.5))

# --- FLEURS JAUNES ---

creer_bloc_fleur_jaune(position=Vec3(-3.75, 1, 3.75))
creer_bloc_fleur_jaune(position=Vec3(-2.75, 1, 1.75))
creer_bloc_fleur_jaune(position=Vec3(-0.5, 1, 2.75))
creer_bloc_fleur_jaune(position=Vec3(-1.5, 1, 4.75))
creer_bloc_fleur_jaune(position=Vec3(-1.75, 1, -1.5))
creer_bloc_fleur_jaune(position=Vec3(4.15, 1, 1.75))
creer_bloc_fleur_jaune(position=Vec3(-5.75, 1, 2.5))

# --- BARRIERE CHENE ---

creer_bloc_barriere(position=Vec3(0.5, 0.5, 3))
creer_bloc_barriere(position=Vec3(0.5, 0.5, 4))
creer_bloc_barriere(position=Vec3(3.5, 0.5, 3))
creer_bloc_barriere(position=Vec3(3.5, 0.5, 4))
creer_bloc_barriere(position=Vec3(1.5, 0.5, 5), rotation_y=90)
creer_bloc_barriere(position=Vec3(2.5, 0.5, 5), rotation_y=90)

# --- BARRIERE ANGLE CHENE ---

creer_bloc_barriere_angle(position=Vec3(0.5, 0.5, 5), rotation_y=0)
creer_bloc_barriere_angle(position=Vec3(3.5, 0.5, 5), rotation_y=90)
creer_bloc_barriere_angle(position=Vec3(3.5, 0.5, 2), rotation_y=180)
creer_bloc_barriere_angle(position=Vec3(0.5, 0.5, 2), rotation_y=270)

# --- BARRIERE SAPIN ---

creer_bloc_barrière_foncé(position=Vec3(-3.5, 3.5, 0), rotation_y=0)
creer_bloc_barrière_foncé(position=Vec3(4.5, 3.5, 0), rotation_y=0)

# --- PORTILLON ---

creer_bloc_portillon(position=Vec3(1.5, 0.5, 2), rotation_y=0)
creer_bloc_portillon(position=Vec3(2.5, 0.5, 2), rotation_y=0)

# --- PILLIER BOIS SAPIN ---

creer_bloc_pillier_foncé(position=Vec3(-3.5, 0.5, -1), rotation_y=0)
creer_bloc_pillier_foncé(position=Vec3(-3.5, 1.5, -1), rotation_y=0)
creer_bloc_pillier_foncé(position=Vec3(-3.5, 2.5, -1), rotation_y=0)
creer_bloc_pillier_foncé(position=Vec3(-3.5, 3.5, -1), rotation_y=0)
creer_bloc_pillier_foncé(position=Vec3(4.5, 0.5, -1), rotation_y=0)
creer_bloc_pillier_foncé(position=Vec3(4.5, 1.5, -1), rotation_y=0)
creer_bloc_pillier_foncé(position=Vec3(4.5, 2.5, -1), rotation_y=0)
creer_bloc_pillier_foncé(position=Vec3(4.5, 3.5, -1), rotation_y=0)

# --- LANTERNE ---

creer_bloc_lanterne(position=Vec3(-3.5, 2.8, 0), rotation_y=0)
creer_bloc_lanterne(position=Vec3(4.5, 2.8, 0), rotation_y=0)

creer_bloc_lanterne(position=Vec3(0.5, 3.8, -15), rotation_y=0)
creer_bloc_lanterne(position=Vec3(0.5, 3.8, -10), rotation_y=0)



# --- COCHON ---

creer_cochon(position=Vec3(2.15, 0.5, 4.25), rotation_y=110)
creer_cochon(position=Vec3(2, 0.5, 2.75), rotation_y=-100)

# --- VILLAGEOIS FERMIER ---

creer_villageois_fermier(position=Vec3(-2, 0.435, 0), rotation_y=-90)

# --- PERROQUET ROUGE ---

creer_perroquet_rouge(position=Vec3(-0.25, 5, 3), rotation_y=-90)
creer_perroquet_rouge(position=Vec3(3.5, 1.5, 2), rotation_y=75)

# --- PERROQUET BLEU ---

creer_perroquet_bleu(position=Vec3(-1.5, 6, 2), rotation_y=105)

# --- PERROQUET GRIS ---

creer_perroquet_gris(position=Vec3(-4.15, 6, 4))

# --- POULET ---

creer_poulet(position=Vec3(3.5, 0.505, -2), rotation_y=-250)
creer_poulet(position=Vec3(-3.5, 0.505, -3), rotation_y=-340)

# --- GOLEM DE FER ---

creer_golem_fer(position=Vec3(-1.95, 0.435, -8), rotation_y=-90)
creer_golem_fer(position=Vec3(2.95, 0.435, -8), rotation_y=90)

# --- RUCHE ---

creer_bloc_ruche(position=Vec3(-5.5, 3.5, -5))

# --- ABEILLE ---

creer_abeille(position=Vec3(-7, 3.5, -5), rotation_y=45)
creer_abeille(position=Vec3(-5.9, 3.5, -4), rotation_y=-135)

# --- LOUP/CHIEN ---

creer_loup(position=Vec3(-2, 0.5, 1),rotation_y=-90)

# ---LAPIN ---

creer_lapin(position=Vec3(-4, 0.5, 3), rotation_y=-90)

# --- BARIERRE SAPIN DEMI ---

creer_bloc_barrière_chene(position=Vec3(-0.5, 4.5, -10), rotation_y=90)
creer_bloc_barrière_chene(position=Vec3(0.5, 4.5, -10), rotation_y=90)
creer_bloc_barrière_chene(position=Vec3(1.5, 4.5, -10), rotation_y=-90)
creer_bloc_barrière_chene(position=Vec3(-0.5, 4.5, -15), rotation_y=90)
creer_bloc_barrière_chene(position=Vec3(0.5, 4.5, -15), rotation_y=90)
creer_bloc_barrière_chene(position=Vec3(1.5, 4.5, -15), rotation_y=-90)
creer_bloc_barrière_chene(position=Vec3(1.5, 3.5, -15), rotation_y=-90)
creer_bloc_barrière_chene(position=Vec3(-0.5, 3.5, -15), rotation_y=-90)
creer_bloc_barrière_chene(position=Vec3(1.5, 3.5, -10), rotation_y=-90)
creer_bloc_barrière_chene(position=Vec3(-0.5, 3.5, -10), rotation_y=-90)
creer_bloc_barrière_chene(position=Vec3(-1.5, 3.5, -15), rotation_y=-90)
creer_bloc_barrière_chene(position=Vec3(-1.5, 3.5, -10), rotation_y=-90)

# --- BARRIERE CHENE MILIEUX  ---

creer_bloc_barrière_chene_milieux(position=Vec3(1, 4.5, -15), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(1.5, 4.5, -15), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(1, 3.5, -15), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(1.5, 3.5, -15), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(1, 4.5, -10), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(1.5, 4.5, -10), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(1, 3.5, -10), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(1.5, 3.5, -10), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(-1.5, 1.5, -15), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(-1.5, 1.5, -10), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(3, 1.5, -10), rotation_y=90)
creer_bloc_barrière_chene_milieux(position=Vec3(3, 1.5, -15), rotation_y=90)

# --- PIERRE LISSE ---

creer_bloc_pierre_lisse(position=Vec3(-2.5, 1.5, -15))
creer_bloc_pierre_lisse(position=Vec3(-2.5, 1.5, -10))
creer_bloc_pierre_lisse(position=Vec3(3.5, 1.5, -15))
creer_bloc_pierre_lisse(position=Vec3(3.5, 1.5, -10))

# --- PIERRE TAILLEE ---

creer_bloc_pierre_taillée(position=Vec3(-4.5, 1.5, -15))
creer_bloc_pierre_taillée(position=Vec3(-4.5, 1.5, -10))
creer_bloc_pierre_taillée(position=Vec3(5.5, 1.5, -15))
creer_bloc_pierre_taillée(position=Vec3(5.5, 1.5, -10))
creer_bloc_pierre_taillée(position=Vec3(-4.5, 4.5, -15))
creer_bloc_pierre_taillée(position=Vec3(-4.5, 4.5, -10))
creer_bloc_pierre_taillée(position=Vec3(5.5, 4.5, -15))
creer_bloc_pierre_taillée(position=Vec3(5.5, 4.5, -10))

EditorCamera()

app.run()