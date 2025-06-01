import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

function LandingPage() {

  const [isVisible, setIsVisible] = useState({
    dependencies: false,
    features: false,
    footer: false
  });
  
  const dependenciesRef = useRef(null);
  const featuresRef = useRef(null);
  const footerRef = useRef(null);

  const navigate = useNavigate();

    // Función para hacer scroll suave al CTA de descarga
  const handleScrollToDownload = () => {
    const section = document.getElementById('download-section');
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
    }
  };
  
  // Intersection Observer to trigger animations on scroll
  useEffect(() => {
    const depsEl = dependenciesRef.current;
    const featsEl = featuresRef.current;
    const footEl = footerRef.current;
  
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.target === depsEl && entry.isIntersecting) {
          setIsVisible(v => ({ ...v, dependencies: true }));
        }
        if (entry.target === featsEl && entry.isIntersecting) {
          setIsVisible(v => ({ ...v, features: true }));
        }
        if (entry.target === footEl && entry.isIntersecting) {
          setIsVisible(v => ({ ...v, footer: true }));
        }
      });
    }, { threshold: 0.2, rootMargin: '0px' });
  
    if (depsEl)  observer.observe(depsEl);
    if (featsEl) observer.observe(featsEl);
    if (footEl)  observer.observe(footEl);
  
    return () => {
      if (depsEl)  observer.unobserve(depsEl);
      if (featsEl) observer.unobserve(featsEl);
      if (footEl)  observer.unobserve(footEl);
    };
  }, []);
  

  const handleRegisterClick = () => {
    navigate('/register');
  };
  return (
    <div className="font-sans bg-gray-50 overflow-x-hidden">
      {/* Header with improved design */}
      <header className="bg-gradient-to-r from-blue-600 to-blue-400 text-white p-4 sticky top-0 z-50 shadow-md">
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <div>
              <img src="icon.png" alt="PokeFarm Logo" className="w-10 h-10 rounded-full" />
            </div>
            <h1 className="text-3xl font-bold tracking-tight">PokeFarm</h1>
          </div>
          
          <nav className="hidden md:flex space-x-8">
            <button 
              onClick={handleRegisterClick}
              className="group relative py-2 px-4 font-medium text-white transition-all duration-300 ease-in-out cursor-pointer"
            >
              Registrarse
              <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-white group-hover:w-full transition-all duration-300 ease-in-out"></span>
            </button>

          </nav>
          
          {/* Mobile menu button */} 
          <div className="md:hidden">
            <button className="p-2 rounded-md hover:bg-blue-700 focus:outline-none">
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>
      </header>

      {/* Hero section with video */}
      <section className="relative h-screen flex items-center justify-center bg-gradient-to-b from-blue-400 to-blue-100">
        {/* Video de fondo sin controles ni branding */}
        <video
          className="absolute inset-0 object-cover w-full h-full"
          src='videobg.mp4' // Reemplaza con la ruta correcta de tu video
          autoPlay
          muted
          loop
          playsInline
        >
          Tu navegador no soporta la etiqueta de video.
        </video>

        {/* Contenido superpuesto */}
        <div className="relative z-10 text-center text-white max-w-4xl mx-auto px-4">
          <h2 className="text-5xl md:text-6xl font-bold mb-6 drop-shadow-lg animate-pulse">
            Automatiza tus farmeos en Pokémon
          </h2>
          <p className="text-xl md:text-2xl mb-8 drop-shadow-md">
            La herramienta definitiva para optimizar tu experiencia de juego
          </p>
          <button
            onClick={handleScrollToDownload}
            className="cursor-pointer bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-full font-bold text-lg transition-all duration-300 transform hover:scale-105 hover:shadow-lg"
          >
            Descargar Ahora
          </button>
        </div>

        <div className="absolute bottom-10 w-full text-center">
          <div className="animate-bounce inline-block">
            <svg className="w-6 h-6 text-white" fill="none" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
            </svg>
          </div>
        </div>
      </section>



      {/* Technology & Dependencies Section */}
      <section 
        ref={dependenciesRef}
        className={`py-20 px-4 bg-white transition-all duration-1000 transform ${
          isVisible.dependencies ? 'translate-x-0 opacity-100' : 'translate-x-100 opacity-0'
        }`}
      
      >
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-16 text-blue-800">Tecnología y Dependencias</h2>
          
          <div className="grid md:grid-cols-2 gap-8">
            <div className="bg-blue-50 p-8 rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300">
              <h3 className="text-2xl font-bold mb-4 text-blue-600">Lenguaje Principal</h3>
              <div className="flex items-center mb-6">
                <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mr-4">
                  <svg className="w-10 h-10 text-blue-600" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07l.01-.13.05-.13.08-.1.11-.07.14-.04.05-.01h2.13l.05.01h6.91zm-6.96 0l-.05.01h-2.13l-.05-.01h2.23z" />
                  </svg>
                </div>
                <div>
                  <h4 className="font-bold text-lg">Python 3.9+</h4>
                  <p className="text-gray-600">Base del sistema de automatización</p>
                </div>
              </div>
              
              <h3 className="text-xl font-bold mb-4 text-blue-600">Características del Entorno</h3>
              <ul className="space-y-2 text-gray-700">
                <li className="flex items-center">
                  <svg className="w-5 h-5 mr-2 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  Multiplataforma (Windows, macOS, Linux)
                </li>
                <li className="flex items-center">
                  <svg className="w-5 h-5 mr-2 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  Lenguaje de alto nivel
                </li>
                <li className="flex items-center">
                  <svg className="w-5 h-5 mr-2 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  Facil de entender y por tanto modificar
                </li>
              </ul>
            </div>
            
            <div className="bg-blue-50 p-8 rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300">
              <h3 className="text-2xl font-bold mb-4 text-blue-600">Bibliotecas Utilizadas</h3>
              <ul className="space-y-4">
                <li className="flex items-start">
                  <span className="inline-flex items-center justify-center h-8 w-8 rounded-md bg-blue-500 text-white mr-3">
                    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </span>
                  <div>
                    <h4 className="font-semibold">PyAutoGUI</h4>
                    <p className="text-gray-600">Control automático del ratón y teclado</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <span className="inline-flex items-center justify-center h-8 w-8 rounded-md bg-blue-500 text-white mr-3">
                    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </span>
                  <div>
                    <h4 className="font-semibold">OpenCV</h4>
                    <p className="text-gray-600">Reconocimiento de imágenes y pantalla</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <span className="inline-flex items-center justify-center h-8 w-8 rounded-md bg-blue-500 text-white mr-3">
                    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </span>
                  <div>
                    <h4 className="font-semibold">Pynput</h4>
                    <p className="text-gray-600">Gestión de hotkeys y eventos de teclado</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <span className="inline-flex items-center justify-center h-8 w-8 rounded-md bg-blue-500 text-white mr-3">
                    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </span>
                  <div>
                    <h4 className="font-semibold">Numpy</h4>
                    <p className="text-gray-600">Procesamiento numérico para análisis de imágenes</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section 
        ref={featuresRef}
        className={`py-20 px-4 bg-gradient-to-r from-blue-50 to-purple-50 transition-all duration-1000 transform ${
          isVisible.features ? 'translate-x-0 opacity-100' : '-translate-x-100 opacity-0'
        }`}
      >
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-16 text-blue-800">Funcionalidades</h2>
          
          <div className="grid md:grid-cols-2 gap-10">
            <div className="bg-white rounded-xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
              <div className="h-48 bg-blue-400 relative overflow-hidden">
                <img src="/capturaMagikarp.png" alt="Magikarp Farming" className="w-full object-cover" />
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end">
                  <h3 className="text-2xl font-bold text-white p-4">Farmeo de Magikarp</h3>
                </div>
              </div>
              <div className="p-6">
                <p className="text-gray-700 mb-4">
                  Automatiza la captura de magikarps en la Zona Safari de Pokemon Rojo Fuego.
                </p>
                <ul className="space-y-2 mb-6">
                  <li className="flex items-center text-gray-600">
                    <svg className="w-4 h-4 mr-2 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    Detección automática de encuentros
                  </li>
                  <li className="flex items-center text-gray-600">
                    <svg className="w-4 h-4 mr-2 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    Manejo de movimiento automaticos
                  </li>
                  <li className="flex items-center text-gray-600">
                    <svg className="w-4 h-4 mr-2 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    Captura automatica
                  </li>
                </ul>
              </div>
            </div>
            
            <div className="bg-white rounded-xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
              <div className="h-48 bg-purple-400 relative overflow-hidden">
                <img src="/imagenHorda.png" alt="XP Farming" className="w-full object-cover" />
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end">
                  <h3 className="text-2xl font-bold text-white p-4">Farmeo de XP</h3>
                </div>
              </div>
              <div className="p-6">
                <p className="text-gray-700 mb-4">
                  Maximiza la ganancia de experiencia de tus Pokémon mediante la automatización de hordas.
                </p>
                <ul className="space-y-2 mb-6">
                  <li className="flex items-center text-gray-600">
                    <svg className="w-4 h-4 mr-2 text-purple-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    Automatico al 100%
                  </li>
                  <li className="flex items-center text-gray-600">
                    <svg className="w-4 h-4 mr-2 text-purple-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    Manejo de evoluciones y habilidades
                  </li>
                  <li className="flex items-center text-gray-600">
                    <svg className="w-4 h-4 mr-2 text-purple-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    Curación automática
                  </li>
                </ul>
              </div>
            </div>
          </div>
          
          <div className="mt-16 bg-white p-8 rounded-xl shadow-lg">
            <h3 className="text-2xl font-bold mb-6 text-blue-700">Características Adicionales</h3>
            
            <div className="grid md:grid-cols-2 gap-8">
              <div className="flex items-start">
                <div className="bg-blue-100 p-3 rounded-full mr-4">
                  <svg className="w-6 h-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
                <div>
                  <h4 className="text-lg font-semibold mb-1">Parada de Emergencia</h4>
                  <p className="text-gray-600">Detén el proceso de farmeo en cualquier momento con solo presionar una tecla.</p>
                </div>
              </div>
              
              <div className="flex items-start">
                <div className="bg-blue-100 p-3 rounded-full mr-4">
                  <svg className="w-6 h-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
                <div>
                  <h4 className="text-lg font-semibold mb-1">Configuración de Hotkeys</h4>
                  <p className="text-gray-600">Personaliza las teclas de acceso rápido según tus preferencias.</p>
                </div>
              </div>
              
              <div className="flex items-start">
                <div className="bg-blue-100 p-3 rounded-full mr-4">
                  <svg className="w-6 h-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>
                <div>
                  <h4 className="text-lg font-semibold mb-1">Estadísticas en Tiempo Real</h4>
                  <p className="text-gray-600">Monitorea la automatización mediante la consola integrada.</p>
                </div>
              </div>
              
              <div className="flex items-start">
                <div className="bg-blue-100 p-3 rounded-full mr-4">
                  <svg className="w-6 h-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                </div>
                <div>
                  <h4 className="text-lg font-semibold mb-1">Adapta las imagenes</h4>
                  <p className="text-gray-600">Elije imagenes de preferencia para otro idiomas.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
        {/* Call to Action Section */}
      <section
        id="download-section"
        className="py-16 px-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white"
      >
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl font-bold mb-6">¡Optimiza tu experiencia de juego ahora!</h2>
          <p className="text-xl mb-10">Únete a otros entrenadores que ya están usando PokeFarm para maximizar su progreso</p>
          
          <div className="flex flex-col sm:flex-row justify-center gap-4">
              <a
                href="/PokeBot.rar"
                download="PokeBot.rar"
                className="bg-white text-blue-600 hover:bg-blue-100 px-8 py-3 rounded-lg font-bold text-lg transition-all duration-300 transform hover:scale-105 cursor-pointer"
              >
                Descargar v0.1
              </a>

          </div>
        </div>
      </section>

      

      {/* FAQ Section */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-16 text-blue-800">Preguntas Frecuentes</h2>
          
          <div className="space-y-6">
            {[
              {
                question: "¿Es legal usar PokeFarm?",
                answer: "PokeFarm está diseñado para automatizar acciones repetitivas y no modifica el juego de ninguna manera. Sin embargo, te recomendamos revisar los términos de servicio del juego en el que lo utilices."
              },
              {
                question: "¿Funciona en todas las versiones de PokeMMO?",
                answer: "Actualmente PokeFarm es compatible con la ultima version Vanilla. Si ha hecho alguna modificacion al juego original es posible que no funcione correctamente."
              },
              {
                question: "¿Necesito conocimientos de programación para usar PokeFarm?",
                answer: "¡No! PokeFarm cuenta con una interfaz gráfica intuitiva que no requiere conocimientos previos de programación."
              },
              {
                question: "¿Puede fallar?",
                answer: "No deberia pasar, per si falla podra detectar mediante la consola cual es el fallo."
              }
            ].map((faq, index) => (
              <div key={index} className="border-b border-gray-200 pb-6">
                <div className="flex justify-between items-start">
                  <h3 className="text-xl font-semibold text-blue-700">{faq.question}</h3>
                  <span className="bg-blue-100 text-blue-800 p-1 rounded-full">
                  </span>
                </div>
                <p className="mt-3 text-gray-600">{faq.answer}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer 
        ref={footerRef}
        className={`bg-cover bg-center relative py-16 px-4 transition-all duration-1000 ease-in-out ${
          isVisible.footer ? 'opacity-100' : 'opacity-0'
        }`}
        style={{ 
          backgroundImage: `linear-gradient(rgba(0, 0, 50, 0.8), rgba(0, 0, 50, 0.9)), url('/api/placeholder/1920/1080')` 
        }}
      >
        <div className="max-w-6xl mx-auto text-white">
          <div className="grid md:grid-cols-4 gap-10">
            <div>
              <h3 className="text-2xl font-bold mb-6 flex items-center">
                <span className="inline-block mr-2">
                  <img src="icon.png" alt="PokeFarm Logo" className="w-8 h-8 rounded-full" />
                </span>
                PokeFarm
              </h3>
              <p className="mb-6 text-blue-200">
                La solución definitiva para optimizar tu experiencia de juego en Pokémon.
              </p>
              <div className="flex space-x-4">
                <a href="#" className="text-white hover:text-blue-300 transition-colors duration-300">
                  <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z" />
                  </svg>
                </a>
                <a href="#" className="text-white hover:text-blue-300 transition-colors duration-300">
                  <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />
                  </svg>
                </a>
                <a href="#" className="text-white hover:text-blue-300 transition-colors duration-300">
                  <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z" />
                  </svg>
                </a>
                <a href="#" className="text-white hover:text-blue-300 transition-colors duration-300">
                  <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                  </svg>
                </a>
              </div>
            </div>
            
            <div>
              <h4 className="text-lg font-semibold mb-4 text-blue-300">Navegación</h4>
              <ul className="space-y-2">
                <li><a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Inicio</a></li>
                <li><a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Características</a></li>
                <li><a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Descargas</a></li>
                <li><a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Documentación</a></li>
                <li><a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Soporte</a></li>
              </ul>
            </div>
            
            <div>
              <h4 className="text-lg font-semibold mb-4 text-blue-300">Recursos</h4>
              <ul className="space-y-2">
                <li><a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Guías y tutoriales</a></li>
                <li><a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Foro de la comunidad</a></li>
                <li><a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Preguntas frecuentes</a></li>
                <li><a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Actualizaciones</a></li>
                <li><a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Blog</a></li>
              </ul>
            </div>
            
            <div>
              <h4 className="text-lg font-semibold mb-4 text-blue-300">Contacto</h4>
              <ul className="space-y-2">
                <li className="flex items-center">
                  <svg className="w-5 h-5 mr-2 text-blue-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                  <a href="mailto:info@pokefarm.app" className="text-blue-100 hover:text-white transition-colors duration-300">info@pokefarm.app</a>
                </li>
                <li className="flex items-center">
                  <svg className="w-5 h-5 mr-2 text-blue-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z" />
                  </svg>
                  <a href="#" className="text-blue-100 hover:text-white transition-colors duration-300">Discord</a>
                </li>
              </ul>
              
    
            </div>
          </div>
          
          <div className="border-t border-blue-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center">
            <p className="text-blue-300">&copy; 2025 PokeFarm. Todos los derechos reservados.</p>
            <div className="flex space-x-6 mt-4 md:mt-0">
              <a href="#" className="text-blue-300 hover:text-white transition-colors duration-300">Política de privacidad</a>
              <a href="#" className="text-blue-300 hover:text-white transition-colors duration-300">Términos de uso</a>
              <a href="#" className="text-blue-300 hover:text-white transition-colors duration-300">Cookies</a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default LandingPage;