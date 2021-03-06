# Generated by Django 3.0.5 on 2020-06-19 09:31

from django.db import migrations, models
import django.db.models.deletion
import polls.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitySector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nom du secteur', max_length=50, unique=True, verbose_name='Nom du secteur')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Nom complet de l'entreprise", max_length=50, unique=True, verbose_name='Nom')),
                ('pdf_name', models.CharField(help_text="nNom de l'entreprise tel que trouvé dans le nom du fichier pdf. Permet en outre de pouvoir automatiser la lecture des PDFs et de les faire correspondre à la bonne entreprise.", max_length=20, unique=True, verbose_name='Nom PDF')),
                ('introduction', models.TextField(default='', help_text="Quelques phrases permettant de décrire brièvement l'entreprise.", verbose_name='Introduction')),
                ('_activity_sectors', models.ManyToManyField(help_text="Secteurs dans lesquels l'entreprise opére", to='polls.ActivitySector', verbose_name='Secteurs')),
            ],
        ),
        migrations.CreateModel(
            name='DPEF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(help_text="Nom complet du pdf de la DPEF, avec extension '.pdf'..", max_length=100, unique=True, verbose_name='Nom du fichier PDF')),
                ('file_object', models.FileField(help_text='Document DPEF ou DDR au format PDF.', unique=True, upload_to='polls/models/dpef/', validators=[polls.models._validate_file_extension], verbose_name='Fichier PDF')),
                ('year', models.IntegerField(choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], help_text='Année de référence du document DPEF', verbose_name='Année')),
                ('company', models.ForeignKey(help_text="L'entreprise référencée par le document.", on_delete=django.db.models.deletion.CASCADE, to='polls.Company', verbose_name='Entreprise')),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Texte de la phrase', verbose_name='Texte')),
                ('text_tokens', models.TextField(help_text='Tokens du texte de la phrase, sous forme de string et séparé par des pipe |', verbose_name='Tokens')),
                ('page', models.PositiveIntegerField(help_text='Page sur laquelle se situe la phrase. Si la phrase est étalée sur plusieur pages, mettre la page de départ.', verbose_name='Page')),
                ('context', models.TextField(help_text='Paragraphe contenant la phrase. Permet de redonner du contexte à la phrase.', verbose_name='Contexte')),
                ('_embedding_vector', models.BinaryField(blank=True, null=True)),
                ('scoring_weight', models.FloatField(help_text='Poids de la phrase, donnée par le poids BM25 de ses constituants.', null=True, verbose_name='Weight')),
                ('dpef', models.ForeignKey(help_text='Document contenant la phrase', on_delete=django.db.models.deletion.CASCADE, to='polls.DPEF', verbose_name='Fichier')),
            ],
        ),
    ]
