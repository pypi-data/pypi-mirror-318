#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* slp.c */
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

#include "slepcnep.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepslpsetdeflationthreshold_ NEPSLPSETDEFLATIONTHRESHOLD
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepslpsetdeflationthreshold_ nepslpsetdeflationthreshold
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepslpgetdeflationthreshold_ NEPSLPGETDEFLATIONTHRESHOLD
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepslpgetdeflationthreshold_ nepslpgetdeflationthreshold
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepslpseteps_ NEPSLPSETEPS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepslpseteps_ nepslpseteps
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepslpgeteps_ NEPSLPGETEPS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepslpgeteps_ nepslpgeteps
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepslpsetepsleft_ NEPSLPSETEPSLEFT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepslpsetepsleft_ nepslpsetepsleft
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepslpgetepsleft_ NEPSLPGETEPSLEFT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepslpgetepsleft_ nepslpgetepsleft
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepslpsetksp_ NEPSLPSETKSP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepslpsetksp_ nepslpsetksp
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepslpgetksp_ NEPSLPGETKSP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepslpgetksp_ nepslpgetksp
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  nepslpsetdeflationthreshold_(NEP nep,PetscReal *deftol, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSLPSetDeflationThreshold(
	(NEP)PetscToPointer((nep) ),*deftol);
}
SLEPC_EXTERN void  nepslpgetdeflationthreshold_(NEP nep,PetscReal *deftol, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLREAL(deftol);
*ierr = NEPSLPGetDeflationThreshold(
	(NEP)PetscToPointer((nep) ),deftol);
}
SLEPC_EXTERN void  nepslpseteps_(NEP nep,EPS eps, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(eps);
*ierr = NEPSLPSetEPS(
	(NEP)PetscToPointer((nep) ),
	(EPS)PetscToPointer((eps) ));
}
SLEPC_EXTERN void  nepslpgeteps_(NEP nep,EPS *eps, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool eps_null = !*(void**) eps ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(eps);
*ierr = NEPSLPGetEPS(
	(NEP)PetscToPointer((nep) ),eps);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! eps_null && !*(void**) eps) * (void **) eps = (void *)-2;
}
SLEPC_EXTERN void  nepslpsetepsleft_(NEP nep,EPS eps, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(eps);
*ierr = NEPSLPSetEPSLeft(
	(NEP)PetscToPointer((nep) ),
	(EPS)PetscToPointer((eps) ));
}
SLEPC_EXTERN void  nepslpgetepsleft_(NEP nep,EPS *eps, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool eps_null = !*(void**) eps ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(eps);
*ierr = NEPSLPGetEPSLeft(
	(NEP)PetscToPointer((nep) ),eps);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! eps_null && !*(void**) eps) * (void **) eps = (void *)-2;
}
SLEPC_EXTERN void  nepslpsetksp_(NEP nep,KSP ksp, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(ksp);
*ierr = NEPSLPSetKSP(
	(NEP)PetscToPointer((nep) ),
	(KSP)PetscToPointer((ksp) ));
}
SLEPC_EXTERN void  nepslpgetksp_(NEP nep,KSP *ksp, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool ksp_null = !*(void**) ksp ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ksp);
*ierr = NEPSLPGetKSP(
	(NEP)PetscToPointer((nep) ),ksp);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ksp_null && !*(void**) ksp) * (void **) ksp = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
