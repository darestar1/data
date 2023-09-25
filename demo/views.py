from django.shortcuts import render, redirect, get_object_or_404
from .models import Observation, Rock, Stream, Soil, OreMicroscopy, Petrograph, XRD, FluidInclusion
from .forms import ObservationForm, RockForm, StreamForm, SoilForm, OreMicroscopyForm, PetrographForm, XRDForm, FluidInclusionForm
from django.urls import reverse

# Tüm gözlemleri listeleme
def observation_list(request):
    observations = Observation.objects.all()
    return render(request, 'observation_list.html', {'observations': observations})

# Yeni bir gözlem oluşturma


from django.shortcuts import render, redirect
from .models import Observation
from .forms import ObservationForm

def observation_create(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('observation_list')  # Gözlem listesine yönlendirme
    else:
        form = ObservationForm()
    
    return render(request, 'observation_create.html', {'form': form})

def observation_list(request):
    observations = Observation.objects.all()
    return render(request, 'observation_list.html', {'observations': observations})

def observation_list_readonly(request):
    observations = Observation.objects.all()
    return render(request, 'observation_list_readonly.html', {'observations': observations})

# Belirli bir gözlemi güncelleme
from django.shortcuts import render, redirect, get_object_or_404
from .models import Observation
from .forms import ObservationUpdateForm

def observation_update_selected(request):
    if request.method == 'POST':
        selected_observation_ids = request.POST.getlist('selected_observation')
        observations = Observation.objects.filter(id__in=selected_observation_ids)
        form = ObservationUpdateForm(request.POST, instance=observations[0])  # Varsayılan olarak bir form oluşturun

        if form.is_valid():
            # Seçilen gözlemleri güncelleme işlemi
            for observation in observations:
                form = ObservationUpdateForm(request.POST, instance=observation)
                form.save()
                
            return redirect('observation_list')  # Gözlem listesine geri dön
        else:
            # Form geçerli değilse, hataları ele alabilirsiniz
            pass
    else:
        return redirect('observation_list')  # POST verisi yoksa, gözlem listesine geri dön

    return render(request, 'observation_list.html', {'observations': Observation.objects.all()})


# Belirli bir gözlemi silme

def home(request):
    return render(request, 'home.html')
def delete_observation(request):
    if request.method == 'POST':
        observation_id = request.POST.get('observation')
        observation = Observation.objects.get(id=observation_id)
        observation.delete()
        return redirect('observation_list')
    
    observations = Observation.objects.all()
    return render(request, 'observation_delete.html', {'observations': observations})




from .forms import ObservationUpdateForm

def observation_update(request, observation_id):
    observation = get_object_or_404(Observation, pk=observation_id)

    if request.method == 'POST':
        form = ObservationUpdateForm(request.POST, instance=observation)
        if form.is_valid():
            form.save()
            return redirect('observation_list')  # Gözlem listesine yönlendirme
    else:
        form = ObservationUpdateForm(instance=observation)

    return render(request, 'observation_update.html', {'form': form, 'observation': observation})



# Rock modeli için işlevler
def rock_list(request):
    rocks = Rock.objects.all()
    return render(request, 'rock_list.html', {'rocks': rocks})

def rock_create(request):
    if request.method == 'POST':
        form = RockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rock_list')
    else:
        form = RockForm()
    return render(request, 'rock_form.html', {'form': form})



# Existing views for list and create are kept as is


def rock_list(request):
    rocks = Rock.objects.all()
    return render(request, 'rock_list.html', {'rocks': rocks})

def rock_update(request, rock_id):
    rock = get_object_or_404(Rock, id=rock_id)

    if request.method == 'POST':
        form = RockForm(request.POST, instance=rock)
        if form.is_valid():
            form.save()
            return redirect('rock_list')  # Rock güncellendikten sonra rock listesine yönlendir
    else:
        form = RockForm(instance=rock)

    return render(request, 'rock_update.html', {'form': form, 'rock': rock})





def delete_rock(request):
    if request.method == 'POST':
        rock_id = request.POST.get('rock')
        rock = Rock.objects.get(id=rock_id)
        rock.delete()
        return redirect('rock_list')

    rocks = Rock.objects.all()
    return render(request, 'rock_delete.html', {'rocks': rocks})


def stream_list(request):
    streams = Stream.objects.all()
    return render(request, 'stream_list.html', {'streams': streams})

def stream_create(request):
    if request.method == 'POST':
        form = StreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stream_list')
    else:
        form = StreamForm()
    return render(request, 'stream_form.html', {'form': form})

def stream_update(request, pk):
    stream = get_object_or_404(Stream, pk=pk)
    if request.method == 'POST':
        form = StreamForm(request.POST, instance=stream)
        if form.is_valid():
            form.save()
            return redirect('stream_list')
    else:
        form = StreamForm(instance=stream)
    return render(request, 'stream_form.html', {'form': form})

def stream_delete(request, pk):
    stream = get_object_or_404(Stream, pk=pk)
    if request.method == 'POST':
        stream.delete()
        return redirect('stream_list')
    return render(request, 'stream_confirm_delete.html', {'stream': stream})

# Soil modeli için görünümler
def soil_list(request):
    soils = Soil.objects.all()
    return render(request, 'soil_list.html', {'soils': soils})

def soil_create(request):
    if request.method == 'POST':
        form = SoilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('soil_list')
    else:
        form = SoilForm()
    return render(request, 'soil_form.html', {'form': form})

def soil_update(request, pk):
    soil = get_object_or_404(Soil, pk=pk)
    if request.method == 'POST':
        form = SoilForm(request.POST, instance=soil)
        if form.is_valid():
            form.save()
            return redirect('soil_list')
    else:
        form = SoilForm(instance=soil)
    return render(request, 'soil_form.html', {'form': form})

def soil_delete(request, pk):
    soil = get_object_or_404(Soil, pk=pk)
    if request.method == 'POST':
        soil.delete()
        return redirect('soil_list')
    return render(request, 'soil_confirm_delete.html', {'soil': soil})
def oremicroscopy_list(request):
    oremicroscopies = OreMicroscopy.objects.all()
    return render(request, 'oremicroscopy_list.html', {'oremicroscopies': oremicroscopies})

def oremicroscopy_create(request):
    if request.method == 'POST':
        form = OreMicroscopyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('oremicroscopy_list')
    else:
        form = OreMicroscopyForm()
    return render(request, 'oremicroscopy_form.html', {'form': form})

def oremicroscopy_update(request, pk):
    oremicroscopy = get_object_or_404(OreMicroscopy, pk=pk)
    if request.method == 'POST':
        form = OreMicroscopyForm(request.POST, instance=oremicroscopy)
        if form.is_valid():
            form.save()
            return redirect('oremicroscopy_list')
    else:
        form = OreMicroscopyForm(instance=oremicroscopy)
    return render(request, 'oremicroscopy_form.html', {'form': form})

def oremicroscopy_delete(request, pk):
    oremicroscopy = get_object_or_404(OreMicroscopy, pk=pk)
    if request.method == 'POST':
        oremicroscopy.delete()
        return redirect('oremicroscopy_list')
    return render(request, 'oremicroscopy_confirm_delete.html', {'oremicroscopy': oremicroscopy})

# Petrograph modeli için görünümler
def petrograph_list(request):
    petrographs = Petrograph.objects.all()
    return render(request, 'petrograph_list.html', {'petrographs': petrographs})

def petrograph_create(request):
    if request.method == 'POST':
        form = PetrographForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('petrograph_list')
    else:
        form = PetrographForm()
    return render(request, 'petrograph_form.html', {'form': form})

def petrograph_update(request, pk):
    petrograph = get_object_or_404(Petrograph, pk=pk)
    if request.method == 'POST':
        form = PetrographForm(request.POST, instance=petrograph)
        if form.is_valid():
            form.save()
            return redirect('petrograph_list')
    else:
        form = PetrographForm(instance=petrograph)
    return render(request, 'petrograph_form.html', {'form': form})

def petrograph_delete(request, pk):
    petrograph = get_object_or_404(Petrograph, pk=pk)
    if request.method == 'POST':
        petrograph.delete()
        return redirect('petrograph_list')
    return render(request, 'petrograph_confirm_delete.html', {'petrograph': petrograph})

# XRD modeli için görünümler
def xrd_list(request):
    xrds = XRD.objects.all()
    return render(request, 'xrd_list.html', {'xrds': xrds})

def xrd_create(request):
    if request.method == 'POST':
        form = XRDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('xrd_list')
    else:
        form = XRDForm()
    return render(request, 'xrd_form.html', {'form': form})

def xrd_update(request, pk):
    xrd = get_object_or_404(XRD, pk=pk)
    if request.method == 'POST':
        form = XRDForm(request.POST, instance=xrd)
        if form.is_valid():
            form.save()
            return redirect('xrd_list')
    else:
        form = XRDForm(instance=xrd)
    return render(request, 'xrd_form.html', {'form': form})

def xrd_delete(request, pk):
    xrd = get_object_or_404(XRD, pk=pk)
    if request.method == 'POST':
        xrd.delete()
        return redirect('xrd_list')
    return render(request, 'xrd_confirm_delete.html', {'xrd': xrd})

# FluidInclusion modeli için görünümler
def fluidinclusion_list(request):
    fluidinclusions = FluidInclusion.objects.all()
    return render(request, 'fluidinclusion_list.html', {'fluidinclusions': fluidinclusions})

def fluidinclusion_create(request):
    if request.method == 'POST':
        form = FluidInclusionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fluidinclusion_list')
    else:
        form = FluidInclusionForm()
    return render(request, 'fluidinclusion_form.html', {'form': form})

def fluidinclusion_update(request, pk):
    fluidinclusion = get_object_or_404(FluidInclusion, pk=pk)
    if request.method == 'POST':
        form = FluidInclusionForm(request.POST, instance=fluidinclusion)
        if form.is_valid():
            form.save()
            return redirect('fluidinclusion_list')
    else:
        form = FluidInclusionForm(instance=fluidinclusion)
    return render(request, 'fluidinclusion_form.html', {'form': form})

def fluidinclusion_delete(request, pk):
    fluidinclusion = get_object_or_404(FluidInclusion, pk=pk)
    if request.method == 'POST':
        fluidinclusion.delete()
        return redirect('fluidinclusion_list')
    return render(request, 'fluidinclusion_confirm_delete.html', {'fluidinclusion': fluidinclusion})