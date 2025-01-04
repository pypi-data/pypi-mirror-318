#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* lyapii.c */
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
#define epslyapiisetranks_ EPSLYAPIISETRANKS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epslyapiisetranks_ epslyapiisetranks
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epslyapiigetranks_ EPSLYAPIIGETRANKS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epslyapiigetranks_ epslyapiigetranks
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epslyapiisetlme_ EPSLYAPIISETLME
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epslyapiisetlme_ epslyapiisetlme
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epslyapiigetlme_ EPSLYAPIIGETLME
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epslyapiigetlme_ epslyapiigetlme
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  epslyapiisetranks_(EPS eps,PetscInt *rkc,PetscInt *rkl, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSLyapIISetRanks(
	(EPS)PetscToPointer((eps) ),*rkc,*rkl);
}
SLEPC_EXTERN void  epslyapiigetranks_(EPS eps,PetscInt *rkc,PetscInt *rkl, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLINTEGER(rkc);
CHKFORTRANNULLINTEGER(rkl);
*ierr = EPSLyapIIGetRanks(
	(EPS)PetscToPointer((eps) ),rkc,rkl);
}
SLEPC_EXTERN void  epslyapiisetlme_(EPS eps,LME lme, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(lme);
*ierr = EPSLyapIISetLME(
	(EPS)PetscToPointer((eps) ),
	(LME)PetscToPointer((lme) ));
}
SLEPC_EXTERN void  epslyapiigetlme_(EPS eps,LME *lme, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool lme_null = !*(void**) lme ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(lme);
*ierr = EPSLyapIIGetLME(
	(EPS)PetscToPointer((eps) ),lme);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! lme_null && !*(void**) lme) * (void **) lme = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
