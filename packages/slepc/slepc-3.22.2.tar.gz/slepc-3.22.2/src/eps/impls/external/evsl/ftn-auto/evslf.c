#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* evsl.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepceps.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsevslsetslices_ EPSEVSLSETSLICES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsevslsetslices_ epsevslsetslices
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsevslgetslices_ EPSEVSLGETSLICES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsevslgetslices_ epsevslgetslices
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsevslsetrange_ EPSEVSLSETRANGE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsevslsetrange_ epsevslsetrange
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsevslgetrange_ EPSEVSLGETRANGE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsevslgetrange_ epsevslgetrange
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsevslsetdosparameters_ EPSEVSLSETDOSPARAMETERS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsevslsetdosparameters_ epsevslsetdosparameters
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsevslgetdosparameters_ EPSEVSLGETDOSPARAMETERS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsevslgetdosparameters_ epsevslgetdosparameters
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsevslsetpolparameters_ EPSEVSLSETPOLPARAMETERS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsevslsetpolparameters_ epsevslsetpolparameters
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsevslgetpolparameters_ EPSEVSLGETPOLPARAMETERS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsevslgetpolparameters_ epsevslgetpolparameters
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsevslsetdamping_ EPSEVSLSETDAMPING
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsevslsetdamping_ epsevslsetdamping
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsevslgetdamping_ EPSEVSLGETDAMPING
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsevslgetdamping_ epsevslgetdamping
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  epsevslsetslices_(EPS eps,PetscInt *nslices, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSEVSLSetSlices(
	(EPS)PetscToPointer((eps) ),*nslices);
}
SLEPC_EXTERN void  epsevslgetslices_(EPS eps,PetscInt *nslices, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLINTEGER(nslices);
*ierr = EPSEVSLGetSlices(
	(EPS)PetscToPointer((eps) ),nslices);
}
SLEPC_EXTERN void  epsevslsetrange_(EPS eps,PetscReal *lmin,PetscReal *lmax, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSEVSLSetRange(
	(EPS)PetscToPointer((eps) ),*lmin,*lmax);
}
SLEPC_EXTERN void  epsevslgetrange_(EPS eps,PetscReal *lmin,PetscReal *lmax, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLREAL(lmin);
CHKFORTRANNULLREAL(lmax);
*ierr = EPSEVSLGetRange(
	(EPS)PetscToPointer((eps) ),lmin,lmax);
}
SLEPC_EXTERN void  epsevslsetdosparameters_(EPS eps,EPSEVSLDOSMethod *dos,PetscInt *nvec,PetscInt *deg,PetscInt *steps,PetscInt *npoints, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSEVSLSetDOSParameters(
	(EPS)PetscToPointer((eps) ),*dos,*nvec,*deg,*steps,*npoints);
}
SLEPC_EXTERN void  epsevslgetdosparameters_(EPS eps,EPSEVSLDOSMethod *dos,PetscInt *nvec,PetscInt *deg,PetscInt *steps,PetscInt *npoints, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLINTEGER(nvec);
CHKFORTRANNULLINTEGER(deg);
CHKFORTRANNULLINTEGER(steps);
CHKFORTRANNULLINTEGER(npoints);
*ierr = EPSEVSLGetDOSParameters(
	(EPS)PetscToPointer((eps) ),dos,nvec,deg,steps,npoints);
}
SLEPC_EXTERN void  epsevslsetpolparameters_(EPS eps,PetscInt *max_deg,PetscReal *thresh, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSEVSLSetPolParameters(
	(EPS)PetscToPointer((eps) ),*max_deg,*thresh);
}
SLEPC_EXTERN void  epsevslgetpolparameters_(EPS eps,PetscInt *max_deg,PetscReal *thresh, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLINTEGER(max_deg);
CHKFORTRANNULLREAL(thresh);
*ierr = EPSEVSLGetPolParameters(
	(EPS)PetscToPointer((eps) ),max_deg,thresh);
}
SLEPC_EXTERN void  epsevslsetdamping_(EPS eps,EPSEVSLDamping *damping, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSEVSLSetDamping(
	(EPS)PetscToPointer((eps) ),*damping);
}
SLEPC_EXTERN void  epsevslgetdamping_(EPS eps,EPSEVSLDamping *damping, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSEVSLGetDamping(
	(EPS)PetscToPointer((eps) ),damping);
}
#if defined(__cplusplus)
}
#endif
