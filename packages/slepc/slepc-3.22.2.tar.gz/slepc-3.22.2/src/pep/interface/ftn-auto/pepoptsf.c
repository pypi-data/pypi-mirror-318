#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* pepopts.c */
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

#include "slepcpep.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetfromoptions_ PEPSETFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetfromoptions_ pepsetfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgettolerances_ PEPGETTOLERANCES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgettolerances_ pepgettolerances
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsettolerances_ PEPSETTOLERANCES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsettolerances_ pepsettolerances
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetdimensions_ PEPGETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetdimensions_ pepgetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetdimensions_ PEPSETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetdimensions_ pepsetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetwhicheigenpairs_ PEPSETWHICHEIGENPAIRS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetwhicheigenpairs_ pepsetwhicheigenpairs
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetwhicheigenpairs_ PEPGETWHICHEIGENPAIRS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetwhicheigenpairs_ pepgetwhicheigenpairs
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetproblemtype_ PEPSETPROBLEMTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetproblemtype_ pepsetproblemtype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetproblemtype_ PEPGETPROBLEMTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetproblemtype_ pepgetproblemtype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetbasis_ PEPSETBASIS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetbasis_ pepsetbasis
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetbasis_ PEPGETBASIS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetbasis_ pepgetbasis
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsettrackall_ PEPSETTRACKALL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsettrackall_ pepsettrackall
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgettrackall_ PEPGETTRACKALL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgettrackall_ pepgettrackall
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetconvergencetest_ PEPSETCONVERGENCETEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetconvergencetest_ pepsetconvergencetest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetconvergencetest_ PEPGETCONVERGENCETEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetconvergencetest_ pepgetconvergencetest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetstoppingtest_ PEPSETSTOPPINGTEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetstoppingtest_ pepsetstoppingtest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetstoppingtest_ PEPGETSTOPPINGTEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetstoppingtest_ pepgetstoppingtest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetscale_ PEPSETSCALE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetscale_ pepsetscale
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetscale_ PEPGETSCALE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetscale_ pepgetscale
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetextract_ PEPSETEXTRACT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetextract_ pepsetextract
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetextract_ PEPGETEXTRACT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetextract_ pepgetextract
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetrefine_ PEPSETREFINE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetrefine_ pepsetrefine
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetrefine_ PEPGETREFINE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetrefine_ pepgetrefine
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetoptionsprefix_ PEPSETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetoptionsprefix_ pepsetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepappendoptionsprefix_ PEPAPPENDOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepappendoptionsprefix_ pepappendoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetoptionsprefix_ PEPGETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetoptionsprefix_ pepgetoptionsprefix
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  pepsetfromoptions_(PEP pep, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetFromOptions(
	(PEP)PetscToPointer((pep) ));
}
SLEPC_EXTERN void  pepgettolerances_(PEP pep,PetscReal *tol,PetscInt *maxits, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLREAL(tol);
CHKFORTRANNULLINTEGER(maxits);
*ierr = PEPGetTolerances(
	(PEP)PetscToPointer((pep) ),tol,maxits);
}
SLEPC_EXTERN void  pepsettolerances_(PEP pep,PetscReal *tol,PetscInt *maxits, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetTolerances(
	(PEP)PetscToPointer((pep) ),*tol,*maxits);
}
SLEPC_EXTERN void  pepgetdimensions_(PEP pep,PetscInt *nev,PetscInt *ncv,PetscInt *mpd, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLINTEGER(nev);
CHKFORTRANNULLINTEGER(ncv);
CHKFORTRANNULLINTEGER(mpd);
*ierr = PEPGetDimensions(
	(PEP)PetscToPointer((pep) ),nev,ncv,mpd);
}
SLEPC_EXTERN void  pepsetdimensions_(PEP pep,PetscInt *nev,PetscInt *ncv,PetscInt *mpd, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetDimensions(
	(PEP)PetscToPointer((pep) ),*nev,*ncv,*mpd);
}
SLEPC_EXTERN void  pepsetwhicheigenpairs_(PEP pep,PEPWhich *which, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetWhichEigenpairs(
	(PEP)PetscToPointer((pep) ),*which);
}
SLEPC_EXTERN void  pepgetwhicheigenpairs_(PEP pep,PEPWhich *which, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPGetWhichEigenpairs(
	(PEP)PetscToPointer((pep) ),which);
}
SLEPC_EXTERN void  pepsetproblemtype_(PEP pep,PEPProblemType *type, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetProblemType(
	(PEP)PetscToPointer((pep) ),*type);
}
SLEPC_EXTERN void  pepgetproblemtype_(PEP pep,PEPProblemType *type, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPGetProblemType(
	(PEP)PetscToPointer((pep) ),type);
}
SLEPC_EXTERN void  pepsetbasis_(PEP pep,PEPBasis *basis, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetBasis(
	(PEP)PetscToPointer((pep) ),*basis);
}
SLEPC_EXTERN void  pepgetbasis_(PEP pep,PEPBasis *basis, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPGetBasis(
	(PEP)PetscToPointer((pep) ),basis);
}
SLEPC_EXTERN void  pepsettrackall_(PEP pep,PetscBool *trackall, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetTrackAll(
	(PEP)PetscToPointer((pep) ),*trackall);
}
SLEPC_EXTERN void  pepgettrackall_(PEP pep,PetscBool *trackall, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPGetTrackAll(
	(PEP)PetscToPointer((pep) ),trackall);
}
SLEPC_EXTERN void  pepsetconvergencetest_(PEP pep,PEPConv *conv, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetConvergenceTest(
	(PEP)PetscToPointer((pep) ),*conv);
}
SLEPC_EXTERN void  pepgetconvergencetest_(PEP pep,PEPConv *conv, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPGetConvergenceTest(
	(PEP)PetscToPointer((pep) ),conv);
}
SLEPC_EXTERN void  pepsetstoppingtest_(PEP pep,PEPStop *stop, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetStoppingTest(
	(PEP)PetscToPointer((pep) ),*stop);
}
SLEPC_EXTERN void  pepgetstoppingtest_(PEP pep,PEPStop *stop, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPGetStoppingTest(
	(PEP)PetscToPointer((pep) ),stop);
}
SLEPC_EXTERN void  pepsetscale_(PEP pep,PEPScale *scale,PetscReal *alpha,Vec Dl,Vec Dr,PetscInt *its,PetscReal *lambda, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(Dl);
CHKFORTRANNULLOBJECT(Dr);
*ierr = PEPSetScale(
	(PEP)PetscToPointer((pep) ),*scale,*alpha,
	(Vec)PetscToPointer((Dl) ),
	(Vec)PetscToPointer((Dr) ),*its,*lambda);
}
SLEPC_EXTERN void  pepgetscale_(PEP pep,PEPScale *scale,PetscReal *alpha,Vec *Dl,Vec *Dr,PetscInt *its,PetscReal *lambda, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLREAL(alpha);
PetscBool Dl_null = !*(void**) Dl ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(Dl);
PetscBool Dr_null = !*(void**) Dr ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(Dr);
CHKFORTRANNULLINTEGER(its);
CHKFORTRANNULLREAL(lambda);
*ierr = PEPGetScale(
	(PEP)PetscToPointer((pep) ),scale,alpha,Dl,Dr,its,lambda);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! Dl_null && !*(void**) Dl) * (void **) Dl = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! Dr_null && !*(void**) Dr) * (void **) Dr = (void *)-2;
}
SLEPC_EXTERN void  pepsetextract_(PEP pep,PEPExtract *extract, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetExtract(
	(PEP)PetscToPointer((pep) ),*extract);
}
SLEPC_EXTERN void  pepgetextract_(PEP pep,PEPExtract *extract, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPGetExtract(
	(PEP)PetscToPointer((pep) ),extract);
}
SLEPC_EXTERN void  pepsetrefine_(PEP pep,PEPRefine *refine,PetscInt *npart,PetscReal *tol,PetscInt *its,PEPRefineScheme *scheme, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetRefine(
	(PEP)PetscToPointer((pep) ),*refine,*npart,*tol,*its,*scheme);
}
SLEPC_EXTERN void  pepgetrefine_(PEP pep,PEPRefine *refine,PetscInt *npart,PetscReal *tol,PetscInt *its,PEPRefineScheme *scheme, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLINTEGER(npart);
CHKFORTRANNULLREAL(tol);
CHKFORTRANNULLINTEGER(its);
*ierr = PEPGetRefine(
	(PEP)PetscToPointer((pep) ),refine,npart,tol,its,scheme);
}
SLEPC_EXTERN void  pepsetoptionsprefix_(PEP pep, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(pep);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = PEPSetOptionsPrefix(
	(PEP)PetscToPointer((pep) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  pepappendoptionsprefix_(PEP pep, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(pep);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = PEPAppendOptionsPrefix(
	(PEP)PetscToPointer((pep) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  pepgetoptionsprefix_(PEP pep, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPGetOptionsPrefix(
	(PEP)PetscToPointer((pep) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for prefix */
*ierr = PetscStrncpy(prefix, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, prefix, cl0);
}
#if defined(__cplusplus)
}
#endif
