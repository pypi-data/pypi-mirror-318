#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* rii.c */
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
#define nepriisetmaximumiterations_ NEPRIISETMAXIMUMITERATIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriisetmaximumiterations_ nepriisetmaximumiterations
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriigetmaximumiterations_ NEPRIIGETMAXIMUMITERATIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriigetmaximumiterations_ nepriigetmaximumiterations
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriisetlagpreconditioner_ NEPRIISETLAGPRECONDITIONER
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriisetlagpreconditioner_ nepriisetlagpreconditioner
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriigetlagpreconditioner_ NEPRIIGETLAGPRECONDITIONER
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriigetlagpreconditioner_ nepriigetlagpreconditioner
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriisetconstcorrectiontol_ NEPRIISETCONSTCORRECTIONTOL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriisetconstcorrectiontol_ nepriisetconstcorrectiontol
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriigetconstcorrectiontol_ NEPRIIGETCONSTCORRECTIONTOL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriigetconstcorrectiontol_ nepriigetconstcorrectiontol
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriisethermitian_ NEPRIISETHERMITIAN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriisethermitian_ nepriisethermitian
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriigethermitian_ NEPRIIGETHERMITIAN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriigethermitian_ nepriigethermitian
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriisetdeflationthreshold_ NEPRIISETDEFLATIONTHRESHOLD
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriisetdeflationthreshold_ nepriisetdeflationthreshold
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriigetdeflationthreshold_ NEPRIIGETDEFLATIONTHRESHOLD
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriigetdeflationthreshold_ nepriigetdeflationthreshold
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriisetksp_ NEPRIISETKSP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriisetksp_ nepriisetksp
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepriigetksp_ NEPRIIGETKSP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepriigetksp_ nepriigetksp
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  nepriisetmaximumiterations_(NEP nep,PetscInt *its, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPRIISetMaximumIterations(
	(NEP)PetscToPointer((nep) ),*its);
}
SLEPC_EXTERN void  nepriigetmaximumiterations_(NEP nep,PetscInt *its, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLINTEGER(its);
*ierr = NEPRIIGetMaximumIterations(
	(NEP)PetscToPointer((nep) ),its);
}
SLEPC_EXTERN void  nepriisetlagpreconditioner_(NEP nep,PetscInt *lag, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPRIISetLagPreconditioner(
	(NEP)PetscToPointer((nep) ),*lag);
}
SLEPC_EXTERN void  nepriigetlagpreconditioner_(NEP nep,PetscInt *lag, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLINTEGER(lag);
*ierr = NEPRIIGetLagPreconditioner(
	(NEP)PetscToPointer((nep) ),lag);
}
SLEPC_EXTERN void  nepriisetconstcorrectiontol_(NEP nep,PetscBool *cct, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPRIISetConstCorrectionTol(
	(NEP)PetscToPointer((nep) ),*cct);
}
SLEPC_EXTERN void  nepriigetconstcorrectiontol_(NEP nep,PetscBool *cct, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPRIIGetConstCorrectionTol(
	(NEP)PetscToPointer((nep) ),cct);
}
SLEPC_EXTERN void  nepriisethermitian_(NEP nep,PetscBool *herm, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPRIISetHermitian(
	(NEP)PetscToPointer((nep) ),*herm);
}
SLEPC_EXTERN void  nepriigethermitian_(NEP nep,PetscBool *herm, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPRIIGetHermitian(
	(NEP)PetscToPointer((nep) ),herm);
}
SLEPC_EXTERN void  nepriisetdeflationthreshold_(NEP nep,PetscReal *deftol, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPRIISetDeflationThreshold(
	(NEP)PetscToPointer((nep) ),*deftol);
}
SLEPC_EXTERN void  nepriigetdeflationthreshold_(NEP nep,PetscReal *deftol, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLREAL(deftol);
*ierr = NEPRIIGetDeflationThreshold(
	(NEP)PetscToPointer((nep) ),deftol);
}
SLEPC_EXTERN void  nepriisetksp_(NEP nep,KSP ksp, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(ksp);
*ierr = NEPRIISetKSP(
	(NEP)PetscToPointer((nep) ),
	(KSP)PetscToPointer((ksp) ));
}
SLEPC_EXTERN void  nepriigetksp_(NEP nep,KSP *ksp, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool ksp_null = !*(void**) ksp ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ksp);
*ierr = NEPRIIGetKSP(
	(NEP)PetscToPointer((nep) ),ksp);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ksp_null && !*(void**) ksp) * (void **) ksp = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
