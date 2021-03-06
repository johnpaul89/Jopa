# Generated by Django 2.1.3 on 2019-02-02 08:26

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('keywords', models.CharField(blank=True, max_length=500, null=True)),
                ('introduction_releasedate', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('introduction_releasedate_image', models.URLField(blank=True, max_length=500, null=True)),
                ('performance_price', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('performance_price_image', models.URLField(blank=True, max_length=500, null=True)),
                ('design_hardware', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('design_hardware_image', models.URLField(blank=True, max_length=500, null=True)),
                ('software_os_softwarefeatures', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('software_os_softwarefeatures_image', models.URLField(blank=True, max_length=500, null=True)),
                ('display', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('display_image', models.URLField(blank=True, max_length=500, null=True)),
                ('batterylife', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('batterylife_image', models.URLField(blank=True, max_length=500, null=True)),
                ('camera', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('camera_image', models.URLField(blank=True, max_length=500, null=True)),
                ('competition', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('competition_image', models.URLField(blank=True, max_length=500, null=True)),
                ('pros', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('pros_image', models.URLField(blank=True, max_length=500, null=True)),
                ('cons', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('cons_image', models.URLField(blank=True, max_length=500, null=True)),
                ('verdict', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('review_image', models.ImageField(blank=True, null=True, upload_to='phonesimages/')),
                ('likes', models.ManyToManyField(blank=True, related_name='reviewlikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('keywords', models.CharField(blank=True, max_length=500, null=True)),
                ('network2G', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('network3G', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('network4G', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('gprsandedge', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('launchannounced', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('launchavailable', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('bodydimensions', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('bodyweight', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('bodybuild', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('bodysim', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('displaytype', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('displaysize', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('displayresolution', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('displaymultitouch', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('displayprotection', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('platformos', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('platformchipset', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('platformcpu', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('platformgpu', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('memorycardslot', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('internalmemory', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('maincameradual', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('maincamerafeatures', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('maincameravideo', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('selfiecameradual', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('selfiecamerafeatures', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('selfiecameravideo', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('soundalerttypes', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('soundloudspeaker', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('soundheadphonejack', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('commswlan', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('commsbluetooth', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('commsgps', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('commsnfc', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('commsradio', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('commsusb', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('featuressensors', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('featuresmessaging', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('featuresbrowser', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('battery', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('devicecolors', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('performancetests', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('displaytest', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('cameratest', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('loudspeakertest', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('audiotest', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('batterytest', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('priceinkenya', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('priceinnigeria', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('priceinsouthafrica', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('otherfeatures', ckeditor.fields.RichTextField()),
                ('specs_image', models.ImageField(blank=True, null=True, upload_to='phonesimages/')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='specslikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.TextField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('review_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devices.PhoneReview')),
                ('review_reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewreplies', to='Devices.ReviewComment')),
                ('review_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewcomments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SpecsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specs_comment', models.TextField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('specs_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devices.PhoneSpecs')),
                ('specs_reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specsreplies', to='Devices.SpecsComment')),
                ('specs_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specscomments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='phonespecs',
            name='tags',
            field=models.ManyToManyField(to='Devices.tags'),
        ),
        migrations.AddField(
            model_name='phonereview',
            name='tags',
            field=models.ManyToManyField(to='Devices.tags'),
        ),
    ]
