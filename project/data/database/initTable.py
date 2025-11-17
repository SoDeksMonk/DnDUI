from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship
import logging

Base = declarative_base()

# Связующие таблицы для отношений many-to-many
features_link = Table('featuresLink', Base.metadata,
    Column('id_classFeatures', Integer, ForeignKey('classFeatures.id'), primary_key=True),
    Column('id_features', Integer, ForeignKey('features.id'), primary_key=True)
)

class_features_link = Table('classFeaturesLink', Base.metadata,
    Column('id_class', Integer, ForeignKey('class.id'), primary_key=True),
    Column('id_classFeatures', Integer, ForeignKey('classFeatures.id'), primary_key=True)
)

class_all_link = Table('classAllLink', Base.metadata,
    Column('id_class', Integer, ForeignKey('class.id'), primary_key=True),
    Column('id_classFeatures', Integer, ForeignKey('classFeatures.id')),
    Column('id_savingThrow', Integer, ForeignKey('savingThrow.id')),
    Column('id_weaponProf', Integer, ForeignKey('weaponProf.id')),
    Column('id_armorProf', Integer, ForeignKey('armorProf.id')),
    Column('id_toolProf', Integer, ForeignKey('toolProf.id'))
)

equipment_all_link = Table('equipmentAllLink', Base.metadata,
    Column('id_equipment', Integer, ForeignKey('equipment.id'), primary_key=True),
    Column('id_weapons', Integer, ForeignKey('weapons.id'), primary_key=True),
    Column('id_armors', Integer, ForeignKey('armors.id'), primary_key=True),
    Column('id_coins', Integer, ForeignKey('coins.id'), primary_key=True)
)

properties_link = Table('propertiesLink', Base.metadata,
    Column('id_weapons', Integer, ForeignKey('weapons.id'), primary_key=True),
    Column('id_properties', Integer, ForeignKey('properties.id'), primary_key=True)
)

legacy_traits_link = Table('legacyTraitsLink', Base.metadata,
    Column('id_legacy', Integer, ForeignKey('legacy.id'), primary_key=True),
    Column('id_legacyTraits', Integer, ForeignKey('legacyTraits.id'), primary_key=True)
)

skill_prof_link = Table('skillProfLink', Base.metadata,
    Column('id_background', Integer, ForeignKey('background.id'), primary_key=True),
    Column('id_skillProf', Integer, ForeignKey('skillProf.id'), primary_key=True)
)

tool_prof_link = Table('toolProfLink', Base.metadata,
    Column('id_toolProf', Integer, ForeignKey('toolProf.id'), primary_key=True),
    Column('id_background', Integer, ForeignKey('background.id')),
    Column('id_class', Integer, ForeignKey('class.id'))
)

traits_link = Table('traitsLink', Base.metadata,
    Column('id_species', Integer, ForeignKey('species.id'), primary_key=True),
    Column('id_traits', Integer, ForeignKey('traits.id'), primary_key=True)
)

# Основные модели
class AbilityBase(Base):
    """The ability table
    """
    __tablename__ = 'ability'
    id = Column(Integer, primary_key=True, autoincrement=True)
    strength = Column(Integer, nullable=False)
    dexterity = Column(Integer, nullable=False)
    constitution = Column(Integer, nullable=False)
    intelligence = Column(Integer, nullable=False)
    wisdom = Column(Integer, nullable=False)
    charisma = Column(Integer, nullable=False)

class AlignmentsBase(Base):
    """the alignments table
    """
    __tablename__ = 'alignments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class ArmorProfBase(Base):
    """the armor profience table
    """
    __tablename__ = 'armorProf'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class ArmorsBase(Base):
    """the armor table
    """
    __tablename__ = 'armors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    armorClass = Column(Integer, nullable=False)
    armorModifier = Column(String)
    needStrength = Column(Integer)
    weight = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)

class BackgroundBase(Base):
    """the background table
    """
    __tablename__ = 'background'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    skillProf = Column(String)
    toolProf = Column(String)

class CharacterBase(Base):
    """the character table
    """
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Integer, nullable=False)
    lvl = Column(Integer, nullable=False)
    id_class = Column(Integer, ForeignKey('class.id'), nullable=False)
    id_ability = Column(Integer, ForeignKey('ability.id'), nullable=False)
    id_alignment = Column(Integer, ForeignKey('alignments.id'), nullable=False)
    languages = Column(String)
    id_equipment = Column(Integer, ForeignKey('equipment.id'), nullable=False)
    id_origins = Column(Integer, ForeignKey('origins.id'), nullable=False)

    # Relationships
    origins = relationship("Origins")
    class_rel = relationship("Class", back_populates="characters")
    ability = relationship("Ability")
    alignment = relationship("Alignments")
    equipment = relationship("Equipment")

class ClassBase(Base):
    """the class table
    """
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    lvl = Column(Integer, nullable=False)  
    HP = Column(Integer, nullable=False)  
    features = Column(Text, nullable=False)
    toolProf = Column(Text, nullable=False)  
    savingThrow = Column(Text, nullable=False)
    weaponProf = Column(Text, nullable=False)
    armorProf = Column(Text, nullable=False)
    
    # Relationships
    characters = relationship("Character", back_populates="class_rel")
    class_features = relationship("ClassFeatures", 
                                  secondary=class_features_link, back_populates="classes")
    saving_throws = relationship("SavingThrow", 
                                 secondary=class_all_link, back_populates="classes")
    weapon_proficiencies = relationship("WeaponProf", 
                                        secondary=class_all_link, back_populates="classes")
    armor_proficiencies = relationship("ArmorProf", 
                                       secondary=class_all_link, back_populates="classes")
    tool_proficiencies = relationship("ToolProf", 
                                      secondary=class_all_link, back_populates="classes")

class ClassFeaturesBase(Base):
    """the table of class features
    """
    __tablename__ = 'classFeatures'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    lvl = Column(Integer, nullable=False)
    bonusProf = Column(Integer, nullable=False)
    features = Column(Text, nullable=False)
    
    # Relationships
    classes = relationship("Class", secondary=class_features_link, 
                           back_populates="class_features")
    features_rel = relationship("Features", secondary=features_link, 
                                back_populates="class_features")

class CoinsBase(Base):
    """the coins table
    """
    __tablename__ = 'coins'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)

class EquipmentBase(Base):
    """the equipment table
    """
    __tablename__ = 'equipment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    weapons = Column(String)
    armor = Column(String)  # Было "name>"
    coins = Column(String)
    
    # Relationships
    weapons_rel = relationship("Weapons", secondary=equipment_all_link, 
                               back_populates="equipment")
    armors_rel = relationship("Armors", secondary=equipment_all_link, 
                              back_populates="equipment")
    coins_rel = relationship("Coins", secondary=equipment_all_link, 
                             back_populates="equipment")

class FeaturesBase(Base):
    """the features table
    """
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    lvl = Column(Integer, nullable=False)
    
    # Relationships
    class_features = relationship("ClassFeatures", secondary=features_link, 
                                  back_populates="features_rel")

class LanguagesBase(Base):
    """the languages table
    """
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class LegacyBase(Base):
    """the legacy table
    """
    __tablename__ = 'legacy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    legacyTraits = Column(String)
    
    # Relationships
    legacy_traits = relationship("LegacyTraits", secondary=legacy_traits_link, back_populates="legacies")

class LegacyTraitsBase(Base):
    """table of legacy features
    """
    __tablename__ = 'legacyTraits'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    lvl = Column(Integer)

class OriginsBase(Base):
    """the origins table
    """
    __tablename__ = 'origins'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_background = Column(Integer, ForeignKey('background.id'), nullable=False)
    id_species = Column(Integer, ForeignKey('species.id'), nullable=False)
    
    # Relationships
    background = relationship("Background")
    species = relationship("Species")

class PropertiesBase(Base):
    """the properties weapons table
    """
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    
    # Relationships
    weapons = relationship("Weapons", secondary=properties_link, back_populates="properties")

class SavingThrowBase(Base):
    """the saving throw table
    """
    __tablename__ = 'savingThrow'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    
    # Relationships
    classes = relationship("Class", secondary=class_all_link, 
                           back_populates="saving_throws")

class SkillProfBase(Base):
    """table of skill profience
    """
    __tablename__ = 'skillProf'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    ability = Column(String)
    description = Column(String)
    
    # Relationships
    backgrounds = relationship("Background", secondary=skill_prof_link, 
                               back_populates="skill_proficiencies")

class SpeciesBase(Base):
    """the species table
    """
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    creatureType = Column(String, nullable=False)
    size = Column(String, nullable=False)
    speed = Column(Integer, nullable=False)
    traits = Column(String)
    id_legacy = Column(Integer, ForeignKey('legacy.id'), nullable=False)
    
    # Relationships
    legacy = relationship("Legacy")
    traits_rel = relationship("Traits", secondary=traits_link, back_populates="species")

class SpellsBase(Base):
    """the spells table
    """
    __tablename__ = 'spells'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    school = Column(String, nullable=False)
    level = Column(Integer)
    slots = Column(Integer, nullable=False)  # Было "sloss"
    special = Column(Integer)

class ToolProfBase(Base):
    """table of tool profience
    """
    __tablename__ = 'toolProf'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    
    # Relationships
    backgrounds = relationship("Background", secondary=tool_prof_link, back_populates="tool_proficiencies")
    classes = relationship("Class", secondary=tool_prof_link, back_populates="tool_proficiencies")

class TraitsBase(Base):
    """the table traits
    """
    __tablename__ = 'traits'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    lvl = Column(Integer)  # Было "id"
    
    # Relationships
    species = relationship("Species", secondary=traits_link, back_populates="traits_rel")

class WeaponProfBase(Base):
    """table of weapon profience 
    """
    __tablename__ = 'weaponProf'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(String)
    description = Column(Text, nullable=False)

class WeaponsBase(Base):
    """the weapons table
    """
    __tablename__ = 'weapons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String)
    type = Column(String)
    damage = Column(String)
    properties = Column(String)
    mastery = Column(String)
    weight = Column(Integer)
    cost = Column(Integer)
    
    # Relationships
    equipment = relationship("Equipment",
                             secondary=equipment_all_link, back_populates="weapons_rel")
    properties_rel = relationship("Properties", 
                                  secondary=properties_link, back_populates="weapons")

# Добавляем отношения для Background
BackgroundBase.skill_proficiencies = relationship("SkillProf", 
                                                  secondary=skill_prof_link, 
                                                  back_populates="backgrounds")
BackgroundBase.tool_proficiencies = relationship("ToolProf", 
                                                 secondary=tool_prof_link, 
                                                 back_populates="backgrounds")

# Создание БД
def create_database(db_url='sqlite:///project/data/database/DnDUIDB.db'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    logging.debug("Database has been created")
    return engine